.RECIPEPREFIX := >

.PHONY: help dev build test autolink autolink-check verify

help:
> @echo "Common targets:"
> @echo "  make dev            - Run Hugo dev server with drafts"
> @echo "  make build          - Build site with minification"
> @echo "  make test           - Run autolink script unit tests"
> @echo "  make autolink       - Apply automatic problem links/relations"
> @echo "  make autolink-check - Check if autolink updates are needed"
> @echo "  make verify         - Run test + autolink-check + build"

dev:
> hugo server -D

build:
> hugo --minify

test:
> uv run python -m unittest scripts/test_auto_link_problems.py

autolink:
> uv run python scripts/auto_link_problems.py

autolink-check:
> uv run python scripts/auto_link_problems.py --check

verify: test autolink-check build
> @echo "Verification complete."
