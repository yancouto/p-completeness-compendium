import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
import re

import sys
from unittest.mock import MagicMock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "auto_link_problems.py"

sys.path.insert(0, str(REPO_ROOT / "scripts"))

# Mock ruamel.yaml to allow importing auto_link_problems for unit tests
# without having to install all dependencies in limited environments.
# This is only done if the module cannot be imported normally.
try:
    import ruamel.yaml
except ImportError:
    mock_yaml = MagicMock()
    sys.modules["ruamel"] = MagicMock()
    sys.modules["ruamel.yaml"] = mock_yaml
    sys.modules["ruamel.yaml.comments"] = MagicMock()

import auto_link_problems


class AutoLinkProblemsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="autolink-test-"))
        problems_dir = self.temp_dir / "content" / "problems"
        problems_dir.mkdir(parents=True, exist_ok=True)
        data_dir = self.temp_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)

        (data_dir / "problem_constraints.yaml").write_text(
            textwrap.dedent(
                """\
                statuses:
                  - p-complete
                  - p-hard
                  - open
                categories:
                  - Circuit Complexity
                  - Graph Theory
                tags:
                  - CC
                  - RNC
                relations:
                  - see-also
                  - reduces-from
                  - reduces-from-variant-of
                  - reduces-to
                  - equivalent
                  - variant
                relation_reciprocals:
                  reduces-from: reduces-to
                  reduces-to: reduces-from
                  equivalent: equivalent
                  variant: variant
                """
            ),
            encoding="utf-8",
        )
        (data_dir / "bibliography.json").write_text(
            json.dumps(
                {
                    "1": {"authors": "Author One", "title": "Ref One", "year": "1991", "doi": None},
                    "2": {"authors": "Author Two", "title": "Ref Two", "year": "1992", "doi": None},
                    "101": {"authors": "Author 101", "title": "Ref 101", "year": "1993", "doi": None},
                    "202": {"authors": "Author 202", "title": "Ref 202", "year": "1994", "doi": None},
                    "303": {"authors": "Author 303", "title": "Ref 303", "year": "1995", "doi": None},
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (problems_dir / "a-1-1.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Circuit Value Problem"
                acronym: 'CVP'
                ---

                ## Remarks

                Canonical base problem.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-1-5.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "NAND Circuit Value Problem"
                acronym: "NANDCVP"
                ---

                ## Remarks

                NORCVP variant definition.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-1.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Sample"
                acronym: "SAMPLE"
                references: [1]
                ---

                ## Remarks

                Reduction is from CVP.
                Already linked [CVP]({{< relref "./a-1-1.md" >}}).
                Also from NORCVP.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-2.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reciprocity Source"
                acronym: "SRC"
                status: "p-complete"
                categories: ["Graph Theory"]
                tags: []
                book_id: "A.2.2"
                related_problems:
                  - id: a-2-3
                    relation: see-also
                  - id: a-2-3
                    relation: reduces-from
                  - id: a-2-4
                    relation: reduces-from-variant-of
                ---

                ## Remarks

                Source node.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-3.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reciprocity Target"
                acronym: "TGT"
                ---

                ## Remarks

                Target node.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-4.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Unrelated Target"
                acronym: "UTGT"
                ---

                ## Remarks

                Target with only see-also.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-8-7.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Sample SC Problem"
                acronym: "SC"
                ---

                ## Remarks

                Defines SC acronym target.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-8-26.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Math Mode Sample"
                acronym: "MMS"
                ---

                ## Remarks

                Inside math: $\\mathsf{SC}^k$ should stay unchanged.
                Outside math: SC should become link.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-9-9.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reference Link Sample"
                acronym: "RLS"
                references: [1, 2]
                book_id: "A.9.9"
                ---

                ## Remarks

                Bounded [1] and [2, Theorem 2.3] are standard.
                Split citations [1][2] should both link.
                Range [1,2] should remain unchanged for now.
                Book citation [3] should link.
                Inside code `[1]` stays.
                Inside math $[1]$ stays.
                Already linked [[1]](#1) stays.
                Malformed [[[1]](1)](#ref-1) should be fixed.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "b-9-9.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reference Normalization Sample"
                acronym: "RNS"
                references: [101, 202, 303]
                book_id: "B.9.9"
                ---

                ## Remarks

                Book citation may stay as [4, Appendix A].
                First non-book is [3, Theorem 2.1].
                Existing linked citation [[1]](#1) should normalize too.
                Then [2] appears.
                """
            ),
            encoding="utf-8",
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--root", str(self.temp_dir), *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )

    def test_check_mode_exits_non_zero_when_changes_needed(self):
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)

    def test_rewrites_body_and_related_problems(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            'Reduction is from [CVP]({{< relref "./a-1-1.md" >}}).',
            updated,
        )
        self.assertIn(
            'Already linked [CVP]({{< relref "./a-1-1.md" >}}).',
            updated,
        )
        self.assertIn(
            'Also from [NORCVP]({{< relref "./a-1-5.md" >}}).',
            updated,
        )
        self.assertIn("related_problems:", updated)
        self.assertIn("- id: a-1-1", updated)
        self.assertIn("- id: a-1-5", updated)
        self.assertIn("relation: see-also", updated)

        second = self.run_script("--check")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)

    def test_preserves_frontmatter_style_and_appends_related_at_end(self):
        original = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(encoding="utf-8")
        original_frontmatter = re.match(
            r"^\ufeff?---\r?\n(?P<front>.*?)(?:\r?\n)---\r?\n",
            original,
            re.DOTALL,
        ).group("front")
        self.assertIn('title: "Sample"', original_frontmatter)
        self.assertIn('acronym: "SAMPLE"', original_frontmatter)
        self.assertIn("references: [1]", original_frontmatter)

        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(encoding="utf-8")
        updated_frontmatter = re.match(
            r"^\ufeff?---\r?\n(?P<front>.*?)(?:\r?\n)---\r?\n",
            updated,
            re.DOTALL,
        ).group("front")

        self.assertIn('title: "Sample"', updated_frontmatter)
        self.assertIn('acronym: "SAMPLE"', updated_frontmatter)
        self.assertIn("references: [1]", updated_frontmatter)
        self.assertTrue(updated_frontmatter.rstrip().endswith("relation: see-also"))

    def test_adds_reciprocal_reduction_relation(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        target_updated = (self.temp_dir / "content" / "problems" / "a-2-3.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("- id: a-2-2", target_updated)
        self.assertIn("relation: reduces-to", target_updated)

    def test_reduction_relations_override_see_also(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        source_updated = (self.temp_dir / "content" / "problems" / "a-2-2.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("- id: a-2-3", source_updated)
        self.assertIn("relation: reduces-from", source_updated)
        self.assertNotIn("- id: a-2-3\n    relation: see-also", source_updated)
        self.assertIn("- id: a-2-4\n    relation: reduces-from-variant-of", source_updated)

        variant_target_updated = (self.temp_dir / "content" / "problems" / "a-2-4.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("- id: a-2-2", variant_target_updated)

    def test_does_not_link_acronyms_inside_latex_math(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-8-26.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Inside math: $\\mathsf{SC}^k$ should stay unchanged.", updated)
        self.assertIn('Outside math: [SC]({{< relref "./a-8-7.md" >}}) should become link.', updated)

    def test_links_in_page_reference_citations(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-9-9.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "Bounded [[1]](#1) and [[2, Theorem 2.3]](#2) are standard.",
            updated,
        )
        self.assertIn(
            "Split citations [[1]](#1)[[2]](#2) should both link.",
            updated,
        )
        self.assertIn("Range [1,2] should remain unchanged for now.", updated)
        self.assertIn(
            "Book citation [[3]](#3) should link.",
            updated,
        )
        self.assertIn("Inside code `[1]` stays.", updated)
        self.assertIn("Inside math $[1]$ stays.", updated)
        self.assertIn("Already linked [[1]](#1) stays.", updated)
        self.assertIn("Malformed [[1]](#1) should be fixed.", updated)

    def test_normalizes_reference_order_by_first_appearance(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "b-9-9.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "Book citation may stay as [[4, Appendix A]](#4).",
            updated,
        )
        self.assertIn(
            "First non-book is [[1, Theorem 2.1]](#1).",
            updated,
        )
        self.assertIn(
            "Existing linked citation [[2]](#2) should normalize too.",
            updated,
        )
        self.assertIn(
            "Then [[3]](#3) appears.",
            updated,
        )
        self.assertRegex(updated, r"references:\s*\[\s*303,\s*101,\s*202\s*\]")

    def test_fails_on_missing_in_page_reference(self):
        (self.temp_dir / "content" / "problems" / "a-3-7.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Bad Reference"
                acronym: "BADREF"
                status: "p-complete"
                categories: ["Graph Theory"]
                tags: []
                book_id: "A.3.7"
                references: [1]
                ---

                ## Remarks

                Uses [3].
                """
            ),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("citation [3] points to missing reference", result.stderr)

    def test_fails_on_unknown_bibliography_reference(self):
        (self.temp_dir / "content" / "problems" / "a-3-8.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Unknown Bibliography Reference"
                acronym: "UNKNOWNREF"
                status: "p-complete"
                categories: ["Graph Theory"]
                tags: []
                book_id: "A.3.8"
                references: [999]
                ---

                ## Remarks

                Uses [[1]](#1).
                """
            ),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown bibliography reference id '999'", result.stderr)

    def test_fails_on_invalid_related_problems_type(self):
        (self.temp_dir / "content" / "problems" / "a-3-9.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Invalid Related Problems Type"
                acronym: "INVALIDRELS"
                status: "p-complete"
                categories: ["Graph Theory"]
                tags: []
                book_id: "A.3.9"
                related_problems: "this should be a list, not a string"
                ---

                ## Remarks

                Content here.
                """
            ),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("'related_problems' must be a YAML list in", result.stderr)



class TestUtilityFunctions(unittest.TestCase):
    def test_merge_spans(self):
        # Empty
        self.assertEqual(auto_link_problems.merge_spans([]), [])

        # Non-overlapping
        self.assertEqual(
            auto_link_problems.merge_spans([(1, 3), (5, 7)]),
            [(1, 3), (5, 7)]
        )

        # Adjoining spans (should be merged)
        self.assertEqual(
            auto_link_problems.merge_spans([(1, 3), (3, 5)]),
            [(1, 5)]
        )

        # Fully contained spans
        self.assertEqual(
            auto_link_problems.merge_spans([(1, 10), (3, 5)]),
            [(1, 10)]
        )

        # Overlapping spans
        self.assertEqual(
            auto_link_problems.merge_spans([(1, 5), (3, 7)]),
            [(1, 7)]
        )

    def test_is_in_spans(self):
        spans = [(1, 5), (10, 15)]

        # Empty
        self.assertFalse(auto_link_problems.is_in_spans(3, []))

        # Before any span
        self.assertFalse(auto_link_problems.is_in_spans(0, spans))

        # In first span
        self.assertTrue(auto_link_problems.is_in_spans(1, spans))
        self.assertTrue(auto_link_problems.is_in_spans(3, spans))

        # End of first span (exclusive)
        self.assertFalse(auto_link_problems.is_in_spans(5, spans))

        # Between spans
        self.assertFalse(auto_link_problems.is_in_spans(7, spans))

        # In second span
        self.assertTrue(auto_link_problems.is_in_spans(12, spans))

        # End of second span (exclusive)
        self.assertFalse(auto_link_problems.is_in_spans(15, spans))

        # After all spans
        self.assertFalse(auto_link_problems.is_in_spans(20, spans))

    def test_format_reference_citation_link(self):
        # Basic case
        self.assertEqual(
            auto_link_problems.format_reference_citation_link(1, ""), "[[1]](#1)"
        )
        # With detail
        self.assertEqual(
            auto_link_problems.format_reference_citation_link(2, ", Theorem 1"),
            "[[2, Theorem 1]](#2)",
        )
        # Number as integer
        self.assertEqual(
            auto_link_problems.format_reference_citation_link(101, "a"), "[[101a]](#101)"
        )

    def test_build_acronym_index(self):
        # Problems with acronyms
        p1 = MagicMock(spec=auto_link_problems.ProblemFile)
        p1.acronym = "ABC"
        p1.path = Path("abc.md")

        p2 = MagicMock(spec=auto_link_problems.ProblemFile)
        p2.acronym = "DEF"
        p2.path = Path("def.md")

        # Problem without acronym
        p3 = MagicMock(spec=auto_link_problems.ProblemFile)
        p3.acronym = None
        p3.path = Path("ghi.md")

        # Problem that is a target for a custom acronym
        # NANDCVP is the target for NORCVP in CUSTOM_ACRONYM_TARGETS
        p4 = MagicMock(spec=auto_link_problems.ProblemFile)
        p4.acronym = "NANDCVP"
        p4.path = Path("nandcvp.md")

        problems = [p1, p2, p3, p4]
        index = auto_link_problems.build_acronym_index(problems)

        self.assertEqual(
            index,
            {
                "ABC": "abc.md",
                "DEF": "def.md",
                "NANDCVP": "nandcvp.md",
                "NORCVP": "nandcvp.md",
            },
        )

    def test_build_acronym_index_empty(self):
        self.assertEqual(auto_link_problems.build_acronym_index([]), {})

class TestErrorPaths(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="autolink-error-test-"))

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_load_problem_constraints_missing_file(self):
        with self.assertRaisesRegex(ValueError, "Missing constraints data file"):
            auto_link_problems.load_problem_constraints(self.temp_dir)

    def test_load_problem_constraints_invalid_yaml(self):
        data_dir = self.temp_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        constraints_file = data_dir / "problem_constraints.yaml"
        constraints_file.write_text("invalid: [yaml: content", encoding="utf-8")

        with self.assertRaises(Exception): # YAML parser error
            auto_link_problems.load_problem_constraints(self.temp_dir)

    def test_load_bibliography_missing_file(self):
        with self.assertRaisesRegex(ValueError, "Missing bibliography data file"):
            auto_link_problems.load_bibliography(self.temp_dir)

    def test_load_bibliography_invalid_json(self):
        data_dir = self.temp_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        bib_file = data_dir / "bibliography.json"
        bib_file.write_text("invalid json", encoding="utf-8")

        with self.assertRaises(ValueError): # JSON decode error
            auto_link_problems.load_bibliography(self.temp_dir)

    def test_load_bibliography_not_a_dict(self):
        data_dir = self.temp_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        bib_file = data_dir / "bibliography.json"
        bib_file.write_text('["not", "a", "dict"]', encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "Bibliography file must be a JSON object"):
            auto_link_problems.load_bibliography(self.temp_dir)

    def test_parse_problem_file_missing_frontmatter(self):
        file_path = self.temp_dir / "no_frontmatter.md"
        file_path.write_text("Just some text.", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "Missing or malformed frontmatter"):
            auto_link_problems.parse_problem_file(file_path)

    def test_parse_problem_file_malformed_frontmatter(self):
        file_path = self.temp_dir / "malformed.md"
        file_path.write_text("---\nmalformed: [yaml\n---\n", encoding="utf-8")

        with self.assertRaises(Exception): # YAML parser error
            auto_link_problems.parse_problem_file(file_path)


if __name__ == "__main__":
    unittest.main()
