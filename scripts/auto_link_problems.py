#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Iterable

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq


FRONTMATTER_PATTERN = re.compile(
    r"^(?P<bom>\ufeff?)(?P<open>---\r?\n)(?P<front>.*?)(?P<close>\r?\n---\r?\n?)(?P<body>.*)$",
    re.DOTALL,
)
EXCLUDED_SPAN_PATTERNS = (
    re.compile(r"(?<!\\)\$\$(?:.|\n)*?(?<!\\)\$\$", re.DOTALL),
    re.compile(r"(?<!\\)\$(?!\$)(?:\\.|[^$\\\n])*(?<!\\)\$(?!\$)"),
    re.compile(r"\\\((?:.|\n)*?\\\)", re.DOTALL),
    re.compile(r"\\\[(?:.|\n)*?\\\]", re.DOTALL),
    re.compile(r"`[^`\n]*`"),
    re.compile(r"!\[[^\]]*\]\([^)]+\)"),
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"<a\b[^>]*>.*?</a>", re.DOTALL | re.IGNORECASE),
    re.compile(r"\{\{<[^>]+>\}\}"),
)
CUSTOM_ACRONYM_TARGETS = {
    "NORCVP": "a-1-5.md",
}
RECIPROCAL_RELATIONS = {
    "reduces-from": "reduces-to",
    "reduces-to": "reduces-from",
}
REFERENCE_CITATION_PATTERN = re.compile(
    r"(?<!\\)\[(?P<num>\d+)(?P<detail>,\s*[^\d\]\s][^\]]*)?\]"
)

YAML_RT = YAML()
YAML_RT.preserve_quotes = True
YAML_RT.indent(mapping=2, sequence=4, offset=2)


@dataclass
class ProblemFile:
    path: Path
    bom: str
    open_delim: str
    close_delim: str
    newline: str
    original_text: str
    frontmatter: CommentedMap
    body: str
    acronym: str | None

    def render(self) -> str:
        stream = StringIO()
        YAML_RT.dump(self.frontmatter, stream)
        dumped = stream.getvalue().rstrip("\n")
        if self.newline == "\r\n":
            dumped = dumped.replace("\n", "\r\n")
        return f"{self.bom}{self.open_delim}{dumped}{self.close_delim}{self.body}"


def parse_problem_file(path: Path) -> ProblemFile:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        raise ValueError(f"Missing or malformed frontmatter in {path}")

    frontmatter_text = match.group("front")
    loaded = YAML_RT.load(frontmatter_text)
    if loaded is None:
        loaded = CommentedMap()
    if not isinstance(loaded, CommentedMap):
        raise ValueError(f"Frontmatter must be a YAML mapping in {path}")

    acronym_value = loaded.get("acronym")
    acronym = str(acronym_value) if acronym_value is not None else None

    return ProblemFile(
        path=path,
        bom=match.group("bom"),
        open_delim=match.group("open"),
        close_delim=match.group("close"),
        newline="\r\n" if "\r\n" in text else "\n",
        original_text=text,
        frontmatter=loaded,
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


def link_acronyms(body: str, acronym_targets: dict[str, str]) -> tuple[str, set[str]]:
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
        linked_problem_ids.add(target_filename.removesuffix(".md"))
        result_parts.append(body[cursor : match.start()])
        result_parts.append(f'[{token}]({{{{< relref "./{target_filename}" >}}}})')
        cursor = match.end()

    if cursor == 0:
        return body, set()

    result_parts.append(body[cursor:])
    return "".join(result_parts), linked_problem_ids


def count_reference_entries(problem: ProblemFile) -> int:
    references = problem.frontmatter.get("references")
    if isinstance(references, list):
        count = len(references)
    elif references is None:
        count = 0
    else:
        count = 1

    book_id = problem.frontmatter.get("book_id")
    if book_id not in (None, ""):
        count += 1
    return count


def link_reference_citations(body: str, reference_count: int) -> str:
    if reference_count <= 0:
        return body

    excluded_spans = build_excluded_spans(body)
    result_parts: list[str] = []
    cursor = 0
    changed = False

    for match in REFERENCE_CITATION_PATTERN.finditer(body):
        if is_in_spans(match.start(), excluded_spans):
            continue

        ref_number = int(match.group("num"))
        if ref_number < 1 or ref_number > reference_count:
            continue

        citation_text = match.group(0)
        result_parts.append(body[cursor : match.start()])
        result_parts.append(
            f'<a href="#ref-{ref_number}" class="reference-citation">{citation_text}</a>'
        )
        cursor = match.end()
        changed = True

    if not changed:
        return body

    result_parts.append(body[cursor:])
    return "".join(result_parts)


def get_related_entries(frontmatter: CommentedMap, source_path: Path, create: bool) -> list[object] | None:
    related = frontmatter.get("related_problems")
    if related is None:
        if not create:
            return None
        related = CommentedSeq()
        frontmatter["related_problems"] = related
        return related
    if not isinstance(related, list):
        raise ValueError(f"'related_problems' must be a YAML list in {source_path}")
    return related


def has_relation_entry(entries: list[object], target_id: str, relation: str) -> bool:
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if str(entry.get("id")) == target_id and str(entry.get("relation")) == relation:
            return True
    return False


def add_relation_entry(problem: ProblemFile, target_id: str, relation: str) -> None:
    entries = get_related_entries(problem.frontmatter, problem.path, create=True)
    assert entries is not None
    if has_relation_entry(entries, target_id, relation):
        return
    entries.append(CommentedMap({"id": target_id, "relation": relation}))


def add_related_problems(problem: ProblemFile, new_problem_ids: set[str]) -> None:
    if not new_problem_ids:
        return
    for problem_id in sorted(new_problem_ids):
        add_relation_entry(problem, problem_id, "see-also")


def prune_see_also_when_reduction_exists(problem: ProblemFile) -> None:
    entries = get_related_entries(problem.frontmatter, problem.path, create=False)
    if entries is None:
        return

    reduction_targets: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        target_id_raw = entry.get("id")
        relation_raw = entry.get("relation")
        if target_id_raw is None or relation_raw is None:
            continue
        if str(relation_raw) in RECIPROCAL_RELATIONS:
            reduction_targets.add(str(target_id_raw))

    if not reduction_targets:
        return

    filtered_entries = CommentedSeq()
    for entry in entries:
        if isinstance(entry, dict):
            target_id_raw = entry.get("id")
            relation_raw = entry.get("relation")
            if (
                target_id_raw is not None
                and relation_raw is not None
                and str(relation_raw) == "see-also"
                and str(target_id_raw) in reduction_targets
            ):
                continue
        filtered_entries.append(entry)

    if len(filtered_entries) != len(entries):
        problem.frontmatter["related_problems"] = filtered_entries


def synchronize_reciprocal_relations(problem_files: list[ProblemFile]) -> None:
    by_problem_id = {problem.path.stem: problem for problem in problem_files}

    for source in problem_files:
        source_entries = get_related_entries(source.frontmatter, source.path, create=False)
        if source_entries is None:
            continue

        for entry in source_entries:
            if not isinstance(entry, dict):
                continue
            target_id_raw = entry.get("id")
            relation_raw = entry.get("relation")
            if target_id_raw is None or relation_raw is None:
                continue

            relation = str(relation_raw)
            reciprocal = RECIPROCAL_RELATIONS.get(relation)
            if reciprocal is None:
                continue

            target_problem = by_problem_id.get(str(target_id_raw))
            if target_problem is None:
                continue
            add_relation_entry(target_problem, source.path.stem, reciprocal)


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
    synchronize_reciprocal_relations(problem_files)
    acronym_index = build_acronym_index(problem_files)

    changed_files: list[Path] = []
    for problem in problem_files:
        current_filename = problem.path.name
        link_targets = {
            acronym: filename
            for acronym, filename in acronym_index.items()
            if filename != current_filename
        }
        reference_count = count_reference_entries(problem)
        body_with_reference_links = link_reference_citations(problem.body, reference_count)
        linked_body, related_problem_ids = link_acronyms(body_with_reference_links, link_targets)
        problem.body = linked_body
        add_related_problems(problem, related_problem_ids)
        prune_see_also_when_reduction_exists(problem)

        updated_text = problem.render()
        if updated_text == problem.original_text:
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
