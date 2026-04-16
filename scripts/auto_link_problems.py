#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
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
HTML_ANCHOR_PATTERN = re.compile(r"<a\b[^>]*>.*?</a>", re.DOTALL | re.IGNORECASE)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\([^)]+\)")
EXCLUDED_SPAN_PATTERNS = (
    re.compile(r"(?<!\\)\$\$(?:.|\n)*?(?<!\\)\$\$", re.DOTALL),
    re.compile(r"(?<!\\)\$(?!\$)(?:\\.|[^$\\\n])*(?<!\\)\$(?!\$)"),
    re.compile(r"\\\((?:.|\n)*?\\\)", re.DOTALL),
    re.compile(r"\\\[(?:.|\n)*?\\\]", re.DOTALL),
    re.compile(r"`[^`\n]*`"),
    re.compile(r"!\[[^\]]*\]\([^)]+\)"),
    MARKDOWN_LINK_PATTERN,
    HTML_ANCHOR_PATTERN,
    re.compile(r"\{\{<[^>]+>\}\}"),
)
# Custom textual acronyms that should link to an existing problem acronym.
# Key: token found in prose, Value: canonical acronym to link to.
CUSTOM_ACRONYM_TARGETS = {
    "NORCVP": "NANDCVP",
}
REFERENCE_CITATION_PATTERN = re.compile(
    r"(?<!\\)\[(?P<num>\d+)(?P<detail>,\s*[^\d\]\s][^\]]*)?\]"
)
REFERENCE_CITATION_TOKEN_PATTERN = re.compile(
    r'(?P<anchor><a href="#ref-(?P<anchor_href_num>\d+)" class="reference-citation">\[(?P<anchor_num>\d+)(?P<anchor_detail>,\s*[^\d\]\s][^\]]*)?\]</a>)'
    r'|(?P<malformed>\[\[\[(?P<malformed_num>\d+)(?P<malformed_detail>,\s*[^\d\]\s][^\]]*)?\]\]\((?P<malformed_inner_num>\d+)\)\]\(#(?:ref-)?(?P<malformed_href_num>\d+)\))'
    r'|(?P<canonical>\[\[(?P<canonical_num>\d+)(?P<canonical_detail>,\s*[^\d\]\s][^\]]*)?\]\]\(#(?P<canonical_href_num>\d+)\))'
    r'|(?P<markdown>\[(?P<markdown_num>\d+)(?P<markdown_detail>,\s*[^\d\]\s][^\]]*)?\]\(#(?:(?:ref-)?)(?P<markdown_href_num>\d+)\))'
    r"|(?P<plain>(?<!\\)\[(?P<plain_num>\d+)(?P<plain_detail>,\s*[^\d\]\s][^\]]*)?\])"
)
BOOK_ID_PATTERN = re.compile(r"^[AB]\.\d+\.\d+$")
PROBLEM_STEM_PATTERN = re.compile(r"^(?P<appendix>[ab])-(?P<section>\d+)-(?P<number>\d+)$")

YAML_RT = YAML()
YAML_RT.preserve_quotes = True
YAML_RT.indent(mapping=2, sequence=4, offset=2)
YAML_SAFE = YAML(typ="safe")


@dataclass(frozen=True)
class ProblemConstraints:
    statuses: set[str]
    categories: set[str]
    tags: set[str]
    relations: set[str]
    relation_reciprocals: dict[str, str]


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


def load_problem_constraints(root: Path) -> ProblemConstraints:
    constraints_path = root / "data" / "problem_constraints.yaml"
    if not constraints_path.is_file():
        raise ValueError(f"Missing constraints data file: {constraints_path}")

    loaded = YAML_SAFE.load(constraints_path.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Constraints file must be a YAML mapping: {constraints_path}")

    statuses = {str(item) for item in loaded.get("statuses", [])}
    categories = {str(item) for item in loaded.get("categories", [])}
    tags = {str(item) for item in loaded.get("tags", [])}
    relations = {str(item) for item in loaded.get("relations", [])}
    relation_reciprocals = {
        str(relation): str(reciprocal)
        for relation, reciprocal in (loaded.get("relation_reciprocals") or {}).items()
    }

    if not statuses:
        raise ValueError("Constraints must define at least one status.")
    if not categories:
        raise ValueError("Constraints must define at least one category.")
    if not relations:
        raise ValueError("Constraints must define at least one relation.")

    invalid_reciprocal_keys = sorted(key for key in relation_reciprocals if key not in relations)
    invalid_reciprocal_values = sorted(
        value for value in relation_reciprocals.values() if value not in relations
    )
    if invalid_reciprocal_keys or invalid_reciprocal_values:
        details: list[str] = []
        if invalid_reciprocal_keys:
            details.append(f"invalid reciprocal keys: {', '.join(invalid_reciprocal_keys)}")
        if invalid_reciprocal_values:
            details.append(f"invalid reciprocal values: {', '.join(invalid_reciprocal_values)}")
        raise ValueError("relation_reciprocals is invalid: " + "; ".join(details))

    return ProblemConstraints(
        statuses=statuses,
        categories=categories,
        tags=tags,
        relations=relations,
        relation_reciprocals=relation_reciprocals,
    )


def load_bibliography(root: Path) -> dict[str, dict[str, object]]:
    bibliography_path = root / "data" / "bibliography.json"
    if not bibliography_path.is_file():
        raise ValueError(f"Missing bibliography data file: {bibliography_path}")

    loaded = json.loads(bibliography_path.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        raise ValueError(f"Bibliography file must be a JSON object: {bibliography_path}")

    bibliography: dict[str, dict[str, object]] = {}
    for key, value in loaded.items():
        key_str = str(key)
        if not isinstance(value, dict):
            raise ValueError(f"Bibliography entry '{key_str}' must be an object")
        bibliography[key_str] = value
    return bibliography


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


def build_excluded_spans(
    text: str,
    *,
    exclude_html_anchors: bool = True,
    exclude_markdown_links: bool = True,
) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    patterns = EXCLUDED_SPAN_PATTERNS
    if not exclude_html_anchors or not exclude_markdown_links:
        patterns = tuple(
            pattern
            for pattern in EXCLUDED_SPAN_PATTERNS
            if (exclude_html_anchors or pattern is not HTML_ANCHOR_PATTERN)
            and (exclude_markdown_links or pattern is not MARKDOWN_LINK_PATTERN)
        )
    for pattern in patterns:
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


def count_non_book_reference_entries(problem: ProblemFile) -> int:
    references = problem.frontmatter.get("references")
    if isinstance(references, list):
        return len(references)
    if references is None:
        return 0
    return 1


def iter_reference_citation_tokens(
    text: str,
) -> Iterable[tuple[int, int, int, str, str]]:
    for match in REFERENCE_CITATION_TOKEN_PATTERN.finditer(text):
        if match.group("anchor") is not None:
            number = int(match.group("anchor_num"))
            detail = match.group("anchor_detail") or ""
            token_kind = "anchor"
        elif match.group("malformed") is not None:
            number = int(match.group("malformed_num"))
            detail = match.group("malformed_detail") or ""
            token_kind = "malformed"
        elif match.group("canonical") is not None:
            number = int(match.group("canonical_num"))
            detail = match.group("canonical_detail") or ""
            token_kind = "canonical"
        elif match.group("markdown") is not None:
            number = int(match.group("markdown_num"))
            detail = match.group("markdown_detail") or ""
            token_kind = "markdown"
        else:
            number = int(match.group("plain_num"))
            detail = match.group("plain_detail") or ""
            token_kind = "plain"
        yield (match.start(), match.end(), number, detail, token_kind)


def format_reference_citation_link(number: int, detail: str) -> str:
    return f"[[{number}{detail}]](#{number})"


def build_reference_normalization_map(
    body: str,
    non_book_reference_count: int,
) -> dict[int, int]:
    if non_book_reference_count <= 1:
        return {}

    excluded_spans = build_excluded_spans(
        body,
        exclude_html_anchors=False,
        exclude_markdown_links=False,
    )
    seen: set[int] = set()
    in_order: list[int] = []

    for start, _, number, _, _ in iter_reference_citation_tokens(body):
        if is_in_spans(start, excluded_spans):
            continue
        if number < 1 or number > non_book_reference_count:
            continue
        if number in seen:
            continue
        seen.add(number)
        in_order.append(number)

    if not in_order:
        return {}

    full_order = in_order + [index for index in range(1, non_book_reference_count + 1) if index not in seen]
    normalization_map = {old_index: new_index for new_index, old_index in enumerate(full_order, start=1)}

    if all(old_index == new_index for old_index, new_index in normalization_map.items()):
        return {}
    return normalization_map


def normalize_reference_citations(
    body: str,
    normalization_map: dict[int, int],
    non_book_reference_count: int,
) -> str:
    if not normalization_map or non_book_reference_count <= 0:
        return body

    excluded_spans = build_excluded_spans(
        body,
        exclude_html_anchors=False,
        exclude_markdown_links=False,
    )
    result_parts: list[str] = []
    cursor = 0
    changed = False

    for start, end, number, detail, _ in iter_reference_citation_tokens(body):
        if is_in_spans(start, excluded_spans):
            continue
        if number < 1 or number > non_book_reference_count:
            continue

        new_number = normalization_map.get(number)
        if new_number is None:
            continue

        result_parts.append(body[cursor:start])
        result_parts.append(format_reference_citation_link(new_number, detail))
        cursor = end
        changed = True

    if not changed:
        return body

    result_parts.append(body[cursor:])
    return "".join(result_parts)


def reorder_references_frontmatter(problem: ProblemFile, normalization_map: dict[int, int]) -> None:
    if not normalization_map:
        return

    references = problem.frontmatter.get("references")
    if not isinstance(references, list):
        return
    if len(references) <= 1:
        return

    ordered_old_indices = [
        old_index
        for old_index, _ in sorted(normalization_map.items(), key=lambda item: item[1])
    ]
    reordered = [references[old_index - 1] for old_index in ordered_old_indices]
    references[:] = reordered


def normalize_reference_order(problem: ProblemFile) -> None:
    non_book_reference_count = count_non_book_reference_entries(problem)
    if non_book_reference_count <= 1:
        return

    normalization_map = build_reference_normalization_map(
        problem.body,
        non_book_reference_count,
    )
    if not normalization_map:
        return

    problem.body = normalize_reference_citations(
        problem.body,
        normalization_map,
        non_book_reference_count,
    )
    reorder_references_frontmatter(problem, normalization_map)


def link_reference_citations(body: str, reference_count: int) -> str:
    if reference_count <= 0:
        return body

    excluded_spans = build_excluded_spans(
        body,
        exclude_html_anchors=False,
        exclude_markdown_links=False,
    )
    result_parts: list[str] = []
    cursor = 0
    changed = False

    for start, end, ref_number, detail, token_kind in iter_reference_citation_tokens(body):
        if is_in_spans(start, excluded_spans):
            continue

        if ref_number < 1 or ref_number > reference_count:
            continue

        replacement = format_reference_citation_link(ref_number, detail)
        original = body[start:end]
        if token_kind == "canonical" and original == replacement:
            continue

        result_parts.append(body[cursor:start])
        result_parts.append(replacement)
        cursor = end
        changed = True

    if not changed:
        return body

    result_parts.append(body[cursor:])
    return "".join(result_parts)


def validate_problem_metadata(
    problem: ProblemFile,
    constraints: ProblemConstraints,
    valid_problem_ids: set[str],
    bibliography: dict[str, dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    prefix = f"{problem.path.name}:"
    frontmatter = problem.frontmatter

    status_raw = frontmatter.get("status")
    if status_raw is not None and str(status_raw) not in constraints.statuses:
        errors.append(f"{prefix} invalid status '{status_raw}'")

    categories = frontmatter.get("categories")
    if categories is not None:
        if not isinstance(categories, list):
            errors.append(f"{prefix} categories must be a YAML list")
        else:
            for category in categories:
                category_name = str(category)
                if category_name not in constraints.categories:
                    errors.append(f"{prefix} invalid category '{category_name}'")

    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append(f"{prefix} tags must be a YAML list")
        else:
            for tag in tags:
                tag_name = str(tag)
                if tag_name not in constraints.tags:
                    errors.append(f"{prefix} invalid tag '{tag_name}'")

    references_value = frontmatter.get("references")
    references = (
        references_value
        if isinstance(references_value, list)
        else ([] if references_value is None else [references_value])
    )
    seen_reference_ids: set[str] = set()
    for reference in references:
        if isinstance(reference, dict):
            ref_id_raw = reference.get("id")
            if ref_id_raw is None:
                continue
            ref_id = str(ref_id_raw)
        else:
            ref_id = str(reference)

        bib_entry = bibliography.get(ref_id)
        if bib_entry is None:
            errors.append(f"{prefix} unknown bibliography reference id '{ref_id}'")
        else:
            for required_field in ("authors", "title", "year"):
                field_value = bib_entry.get(required_field)
                if field_value is None or str(field_value).strip() == "":
                    errors.append(
                        f"{prefix} bibliography entry '{ref_id}' missing '{required_field}'"
                    )
        if ref_id in seen_reference_ids:
            errors.append(f"{prefix} duplicate reference id '{ref_id}'")
        seen_reference_ids.add(ref_id)

    related_entries = get_related_entries(frontmatter, problem.path, create=False)
    if related_entries is not None:
        seen_relations: set[tuple[str, str]] = set()
        for entry in related_entries:
            if not isinstance(entry, dict):
                errors.append(f"{prefix} related_problems entries must be objects")
                continue

            target_id_raw = entry.get("id")
            relation_raw = entry.get("relation")
            if target_id_raw is None:
                errors.append(f"{prefix} related_problems entry missing id")
                continue
            if relation_raw is None:
                errors.append(f"{prefix} related_problems entry missing relation for id '{target_id_raw}'")
                continue

            target_id = str(target_id_raw)
            relation = str(relation_raw)
            if relation not in constraints.relations:
                errors.append(f"{prefix} invalid related_problems relation '{relation}' for id '{target_id}'")
            if target_id not in valid_problem_ids:
                errors.append(f"{prefix} related problem '{target_id}' does not exist")
            if target_id == problem.path.stem:
                errors.append(f"{prefix} related problem points to itself ('{target_id}')")

            relation_key = (target_id, relation)
            if relation_key in seen_relations:
                errors.append(f"{prefix} duplicate related_problems entry id='{target_id}' relation='{relation}'")
            seen_relations.add(relation_key)

    reference_count = count_reference_entries(problem)
    excluded_spans = build_excluded_spans(
        problem.body,
        exclude_html_anchors=False,
        exclude_markdown_links=False,
    )
    for start, _, citation_number, _, _ in iter_reference_citation_tokens(problem.body):
        if is_in_spans(start, excluded_spans):
            continue
        if citation_number < 1 or citation_number > reference_count:
            errors.append(
                f"{prefix} citation [{citation_number}] points to missing reference "
                f"(available: 1..{reference_count})"
            )

    book_id_raw = frontmatter.get("book_id")
    if book_id_raw is not None and str(book_id_raw).strip() != "":
        book_id = str(book_id_raw)
        if BOOK_ID_PATTERN.match(book_id) is None:
            errors.append(f"{prefix} invalid book_id format '{book_id}'")
        stem_match = PROBLEM_STEM_PATTERN.match(problem.path.stem)
        if stem_match is not None:
            expected_book_id = (
                f"{stem_match.group('appendix').upper()}."
                f"{stem_match.group('section')}."
                f"{stem_match.group('number')}"
            )
            if book_id != expected_book_id:
                errors.append(
                    f"{prefix} book_id '{book_id}' does not match filename-derived id '{expected_book_id}'"
                )

    stem_match = PROBLEM_STEM_PATTERN.match(problem.path.stem)
    if stem_match is not None and status_raw is not None:
        appendix = stem_match.group("appendix")
        status = str(status_raw)
        if appendix == "b" and status != "open":
            errors.append(f"{prefix} appendix B problem must have status 'open' (found '{status}')")
        if appendix == "a" and status == "open":
            errors.append(f"{prefix} appendix A problem cannot have status 'open'")

    return errors


def validate_global_metadata(problem_files: list[ProblemFile]) -> list[str]:
    errors: list[str] = []
    by_acronym: dict[str, list[str]] = {}
    for problem in problem_files:
        if not problem.acronym:
            continue
        by_acronym.setdefault(problem.acronym, []).append(problem.path.name)

    for acronym, files in sorted(by_acronym.items()):
        if len(files) > 1:
            errors.append(f"duplicate acronym '{acronym}' in files: {', '.join(sorted(files))}")
    return errors


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


def prune_see_also_when_reduction_exists(
    problem: ProblemFile,
    reciprocal_relations: dict[str, str],
) -> None:
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
        if str(relation_raw) in reciprocal_relations:
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


def synchronize_reciprocal_relations(
    problem_files: list[ProblemFile],
    reciprocal_relations: dict[str, str],
) -> None:
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
            reciprocal = reciprocal_relations.get(relation)
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

    for custom_acronym, target_acronym in CUSTOM_ACRONYM_TARGETS.items():
        target_filename = index.get(target_acronym)
        if target_filename is not None:
            index[custom_acronym] = target_filename
    return index


def run(root: Path, check: bool) -> int:
    problems_dir = root / "content" / "problems"
    if not problems_dir.is_dir():
        print(f"Problems directory not found: {problems_dir}", file=sys.stderr)
        return 2
    constraints = load_problem_constraints(root)
    bibliography = load_bibliography(root)

    paths = sorted(path for path in problems_dir.glob("*.md") if path.name != "_index.md")
    problem_files = [parse_problem_file(path) for path in paths]
    valid_problem_ids = {problem.path.stem for problem in problem_files}
    synchronize_reciprocal_relations(problem_files, constraints.relation_reciprocals)
    acronym_index = build_acronym_index(problem_files)

    changed_files: list[Path] = []
    rendered_updates: dict[Path, str] = {}
    validation_errors: list[str] = []
    for problem in problem_files:
        current_filename = problem.path.name
        normalize_reference_order(problem)
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
        prune_see_also_when_reduction_exists(problem, constraints.relation_reciprocals)
        validation_errors.extend(
            validate_problem_metadata(
                problem,
                constraints=constraints,
                valid_problem_ids=valid_problem_ids,
                bibliography=bibliography,
            )
        )

        updated_text = problem.render()
        if updated_text == problem.original_text:
            continue
        changed_files.append(problem.path)
        rendered_updates[problem.path] = updated_text

    validation_errors.extend(validate_global_metadata(problem_files))
    if validation_errors:
        shown_errors = validation_errors[:200]
        message = ["Validation failed:"] + [f"- {error}" for error in shown_errors]
        if len(validation_errors) > len(shown_errors):
            message.append(
                f"- ... and {len(validation_errors) - len(shown_errors)} more validation errors"
            )
        raise ValueError("\n".join(message))

    if changed_files and not check:
        for path in changed_files:
            problem_text = rendered_updates.get(path)
            assert problem_text is not None
            path.write_text(problem_text, encoding="utf-8")

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
