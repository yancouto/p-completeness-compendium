# P-Complete Problems Compendium

A searchable compendium of **P-complete problems** — computational problems believed to have no efficient parallel algorithms.

🌐 **[View the live site](https://yancouto.github.io/p-completeness-compendium/)**

## Running Locally

Requires [Hugo](https://gohugo.io/installation/) (extended version, v0.110+).

```bash
git clone https://github.com/yancouto/p-completeness-compendium.git
cd p-completeness-compendium
hugo server -D
# Open http://localhost:1313
```

## Autolink script

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync --locked
uv run python scripts/auto_link_problems.py
uv run python scripts/auto_link_problems.py --check
uv run python -m unittest scripts/test_auto_link_problems.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) or the [About page](https://yancouto.github.io/p-completeness-compendium/about/#contributing) on the website.

## License

This project is open source. Problem descriptions are based on published academic research.
