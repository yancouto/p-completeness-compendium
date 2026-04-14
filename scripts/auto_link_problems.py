#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


FRONTMATTER_PATTERN = re.compile(
    r"^(?P<bom>\ufeff?)(?P<open>---\r?\n)(?P<front>.*?)(?P<close>\r?\n---\r?\n?)(?P<body>.*)$",
    re.DOTALL,
)
ACRONYM_PATTERN = re.compile(r'(?m)^acronym:\s*"?(?P<acronym>[A-Z0-9]+)"?\s*$')
RELATED_PROBLEM_ID_PATTERN = re.compile(r'(?m)^\s*-\s*id:\s*"?(?P<id>[a-z]-\d+-\d+)"?\s*$')
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
    open_delim: str
    frontmatter: str
    close_delim: str
    body: str
    acronym: str | None

    @property
    def newline(self) -> str:
        return "\r\n" if "\r\n" in self.open_delim else "\n"

    def render(self, frontmatter: str, body: str) -> str:
        return f"{self.bom}{self.open_delim}{frontmatter}{self.close_delim}{body}"


def parse_problem_file(path: Path) -> ProblemFile:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        raise ValueError(f"Missing or malformed frontmatter in {path}")

    frontmatter = match.group("front")
    acronym_match = ACRONYM_PATTERN.search(frontmatter)
    acronym = acronym_match.group("acronym") if acronym_match else None

    return ProblemFile(
        path=path,
        bom=match.group("bom"),
        open_delim=match.group("open"),
        frontmatter=frontmatter,
        close_delim=match.group("close"),
        body=match.group("body"),
        acronym=acronym,
    )


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


def add_related_problems(frontmatter: str, new_problem_ids: set[str], newline: str) -> str:
    if not new_problem_ids:
        return frontmatter

    existing_ids = {match.group("id") for match in RELATED_PROBLEM_ID_PATTERN.finditer(frontmatter)}
    to_add = [problem_id for problem_id in sorted(new_problem_ids) if problem_id not in existing_ids]
    if not to_add:
        return frontmatter

    lines = frontmatter.splitlines(keepends=True)
    if not lines:
        lines = [newline]

    if lines[-1] and not lines[-1].endswith(("\n", "\r")):
        lines[-1] = f"{lines[-1]}{newline}"

    related_index = next(
        (index for index, line in enumerate(lines) if line.strip() == "related_problems:"),
        None,
    )

    insertion_lines: list[str] = []
    for problem_id in to_add:
        insertion_lines.append(f"  - id: {problem_id}{newline}")
        insertion_lines.append(f"    relation: see-also{newline}")

    if related_index is None:
        lines.append(f"related_problems:{newline}")
        lines.extend(insertion_lines)
        return "".join(lines).rstrip("\r\n")

    insert_at = related_index + 1
    while insert_at < len(lines):
        current = lines[insert_at]
        if current.startswith("  ") or current.strip() == "":
            insert_at += 1
            continue
        break
    lines[insert_at:insert_at] = insertion_lines
    return "".join(lines).rstrip("\r\n")


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

        linked_body, related_problem_ids = link_acronyms(problem.body, link_targets)
        updated_frontmatter = add_related_problems(
            problem.frontmatter,
            related_problem_ids,
            problem.newline,
        )
        updated_text = problem.render(updated_frontmatter, linked_body)
        original_text = problem.render(problem.frontmatter, problem.body)

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
