#!/usr/bin/env python
from __future__ import annotations

import argparse
import copy
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import frontmatter


EXCLUDED_SPAN_PATTERNS = (
    re.compile(r"`[^`\n]*`"),
    re.compile(r"!\[[^\]]*\]\([^)]+\)"),
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"\{\{<[^>]+>\}\}"),
)
CUSTOM_ACRONYM_TARGETS = {
    "NORCVP": "a-1-5.md",
}


@dataclass
class ProblemFile:
    path: Path
    bom: str
    newline: str
    post: frontmatter.Post
    acronym: str | None

    def render(self, post: frontmatter.Post) -> str:
        rendered = frontmatter.dumps(post)
        if self.newline == "\r\n":
            rendered = rendered.replace("\n", "\r\n")
        return f"{self.bom}{rendered}"


def parse_problem_file(path: Path) -> ProblemFile:
    text = path.read_text(encoding="utf-8")
    bom = "\ufeff" if text.startswith("\ufeff") else ""
    text_without_bom = text[len(bom) :]
    newline = "\r\n" if "\r\n" in text else "\n"

    if not text_without_bom.startswith("---"):
        raise ValueError(f"Missing or malformed frontmatter in {path}")

    try:
        post = frontmatter.loads(text_without_bom)
    except Exception as error:  # pragma: no cover - parser-specific exceptions
        raise ValueError(f"Missing or malformed frontmatter in {path}: {error}") from error

    acronym_value = post.metadata.get("acronym")
    acronym = str(acronym_value) if acronym_value is not None else None

    return ProblemFile(
        path=path,
        bom=bom,
        newline=newline,
        post=post,
        acronym=acronym,
    )


def clone_post(post: frontmatter.Post) -> frontmatter.Post:
    return frontmatter.Post(post.content, **copy.deepcopy(post.metadata))


def merge_spans(spans: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    ordered = sorted(spans)
    if not ordered:
        return []

    merged: list[tuple[int, int]] = [ordered[0]]
    for start, end in ordered[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
            continue
        merged.append((start, end))
    return merged


def is_in_spans(index: int, spans: list[tuple[int, int]]) -> bool:
    for start, end in spans:
        if start <= index < end:
            return True
        if index < start:
            return False
    return False


def build_excluded_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pattern in EXCLUDED_SPAN_PATTERNS:
        spans.extend((match.start(), match.end()) for match in pattern.finditer(text))
    return merge_spans(spans)


def link_acronyms(
    body: str,
    acronym_targets: dict[str, str],
) -> tuple[str, set[str]]:
    if not acronym_targets:
        return body, set()

    escaped_tokens = sorted((re.escape(token) for token in acronym_targets), key=len, reverse=True)
    token_pattern = re.compile(rf"(?<![A-Z0-9])(?P<token>{'|'.join(escaped_tokens)})(?![A-Z0-9])")
    excluded_spans = build_excluded_spans(body)
    linked_problem_ids: set[str] = set()
    result_parts: list[str] = []
    cursor = 0

    for match in token_pattern.finditer(body):
        if is_in_spans(match.start(), excluded_spans):
            continue

        token = match.group("token")
        target_filename = acronym_targets[token]
        target_problem_id = target_filename.removesuffix(".md")
        linked_problem_ids.add(target_problem_id)

        result_parts.append(body[cursor : match.start()])
        result_parts.append(f'[{token}]({{{{< relref "./{target_filename}" >}}}})')
        cursor = match.end()

    if cursor == 0:
        return body, set()

    result_parts.append(body[cursor:])
    return "".join(result_parts), linked_problem_ids


def add_related_problems(
    post: frontmatter.Post,
    new_problem_ids: set[str],
    source_path: Path,
) -> frontmatter.Post:
    if not new_problem_ids:
        return post

    updated_post = clone_post(post)
    related_value = updated_post.metadata.get("related_problems")
    if related_value is None:
        related_entries: list[object] = []
    elif isinstance(related_value, list):
        related_entries = related_value
    else:
        raise ValueError(f"'related_problems' must be a YAML list in {source_path}")

    existing_ids: set[str] = set()
    for entry in related_entries:
        if isinstance(entry, dict):
            entry_id = entry.get("id")
            if entry_id is not None:
                existing_ids.add(str(entry_id))
        elif isinstance(entry, str):
            existing_ids.add(entry)

    to_add = [problem_id for problem_id in sorted(new_problem_ids) if problem_id not in existing_ids]
    if not to_add:
        return post

    for problem_id in to_add:
        related_entries.append({"id": problem_id, "relation": "see-also"})

    updated_post.metadata["related_problems"] = related_entries
    return updated_post


def build_acronym_index(problem_files: list[ProblemFile]) -> dict[str, str]:
    index: dict[str, str] = {}
    for problem in problem_files:
        if not problem.acronym:
            continue
        index[problem.acronym] = problem.path.name

    for custom_acronym, target in CUSTOM_ACRONYM_TARGETS.items():
        index[custom_acronym] = target
    return index


def run(root: Path, check: bool) -> int:
    problems_dir = root / "content" / "problems"
    if not problems_dir.is_dir():
        print(f"Problems directory not found: {problems_dir}", file=sys.stderr)
        return 2

    paths = sorted(path for path in problems_dir.glob("*.md") if path.name != "_index.md")
    problem_files = [parse_problem_file(path) for path in paths]
    acronym_index = build_acronym_index(problem_files)

    changed_files: list[Path] = []
    for problem in problem_files:
        current_filename = problem.path.name
        link_targets = {
            acronym: filename
            for acronym, filename in acronym_index.items()
            if filename != current_filename
        }

        linked_body, related_problem_ids = link_acronyms(problem.post.content, link_targets)
        updated_post = add_related_problems(problem.post, related_problem_ids, problem.path)
        if linked_body != updated_post.content:
            updated_post.content = linked_body

        updated_text = problem.render(updated_post)
        original_text = problem.render(problem.post)

        if updated_text == original_text:
            continue

        changed_files.append(problem.path)
        if not check:
            problem.path.write_text(updated_text, encoding="utf-8")

    if changed_files:
        for path in changed_files:
            print(path.relative_to(root).as_posix())
        print(f"Changed files: {len(changed_files)}")
        return 1 if check else 0

    print("No changes needed.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Auto-link problem acronyms and maintain related_problems frontmatter."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root containing content/problems",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write files. Exit non-zero when changes are needed.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        return run(args.root.resolve(), check=args.check)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
