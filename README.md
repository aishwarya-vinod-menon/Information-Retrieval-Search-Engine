# Information Retrieval Search Engine (Academic Project)

A cleaned-up, reproducible portfolio version of an academic IR system using:

- Apache Nutch for crawling
- Apache Solr for indexing and retrieval
- Flask backend API
- JavaScript frontend
- IR features: PageRank, HITS, query expansion, and clustering

> This is **not** presented as production-ready software. It is a refactored course project for learning and demonstration.

## Repository structure

```text
app/
  main.py
  config.py
  services/
  utils/
frontend/
  index.html
  script.js
  style.css
data/
  processed/
docs/
archive/
  legacy/
requirements.txt
.env.example
.gitignore
README.md
```

## Quick start

1. Create virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure environment:

```bash
cp .env.example .env
```

3. Ensure Solr is running locally with a populated `nutch` core:

`http://localhost:8983/solr/nutch`

4. Run backend API:

```bash
python -m app.main
```

5. Open `frontend/index.html` in your browser (or serve it with any static server).

## Feature mapping

- `page_rank` → rerank Solr results using precomputed PageRank scores.
- `hits` → rerank Solr results using precomputed HITS scores.
- `flat_clustering`, `single_hac`, `average_hac` → cluster-aware result ordering.
- `association_qe`, `metric_qe`, `scalar_qe` → query expansion then retrieval.

## Legacy materials

Original scripts and files were preserved in `archive/legacy/` for traceability.

See `docs/notes.md` for artifact expectations and runtime assumptions.
