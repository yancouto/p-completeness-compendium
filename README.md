# P-Complete Problems Compendium

A searchable, collaborative compendium of **P-complete problems** — computational problems that are believed to have no efficient parallel algorithms.

🌐 **[View the live site](https://yourusername.github.io/p-complete-compendium/)**

## About

This project catalogs problems from computational complexity theory that are **P-complete**. Just as NP-complete problems are believed to have no efficient sequential algorithms, P-complete problems are believed to have no efficient *parallel* algorithms (i.e., they are not in NC unless P = NC).

The compendium is based on the comprehensive catalog from:

> Greenlaw, R., Hoover, H. J., & Ruzzo, W. L. (1995). *Limits to Parallel Computation: P-Completeness Theory*. Oxford University Press.

## Features

- 📚 **Comprehensive catalog** of P-complete and open problems
- 🔍 **Search and filter** by name, category, status, or tags
- 📐 **LaTeX math support** via KaTeX
- 🔗 **Problem relationships** showing reductions and variants
- 📖 **Detailed references** to original papers

## Running Locally

### Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended version, v0.110+)

### Development

```bash
# Clone the repository
git clone https://github.com/yourusername/p-complete-compendium.git
cd p-complete-compendium

# Start the development server
hugo server -D

# Open http://localhost:1313
```

### Building

```bash
hugo --minify
# Output is in the `public/` directory
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding new problems
- Improving existing descriptions
- Reporting errors
- General documentation

## Project Structure

```
p-complete-compendium/
├── content/
│   ├── problems/          # Problem definitions (Markdown + YAML)
│   │   ├── a-1-1-cvp.md   # Circuit Value Problem
│   │   ├── a-2-3-agap.md  # Alternating Graph Accessibility
│   │   └── ...
│   ├── about.md           # About page
│   └── _index.md          # Homepage
├── layouts/               # Hugo templates
├── static/
│   ├── css/style.css      # Styles
│   └── js/search.js       # Client-side search
├── hugo.toml              # Hugo configuration
└── .github/workflows/     # GitHub Actions for deployment
```

## Categories

The problems are organized following the book's structure:

**P-Complete (Appendix A):**
- A.1 Circuit Complexity
- A.2 Graph Theory
- A.3 Searching Graphs
- A.4 Combinatorial Optimization
- A.5 Local Optimality
- A.6 Logic
- A.7 Formal Languages
- A.8 Algebra
- A.9 Geometry
- A.10 Real Analysis
- A.11 Games
- A.12 Miscellaneous

**Open Problems (Appendix B):** Problems whose P-completeness or membership in NC is unknown.

## License

This project is open source. The problem descriptions are based on published academic research.

## Acknowledgments

- The foundational work by Greenlaw, Hoover, and Ruzzo
- All researchers who have contributed to P-completeness theory
- Contributors to this open-source project
