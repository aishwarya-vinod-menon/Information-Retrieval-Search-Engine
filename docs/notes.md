# Project notes

This repository is an **academic Information Retrieval project** and is kept portfolio-ready for reproducibility.

## Live search dependency

The Flask API expects a **local Apache Solr core named `nutch`** available at:

`http://localhost:8983/solr/nutch`

Without this populated core, live query responses will be empty or fail.

## Expected generated artifacts under `data/processed/`

- `r_modified_scores.txt` (PageRank scores)
- `hits_scores.txt` (HITS scores)
- `tfidfVec.pkl` (TF-IDF vectorizer)
- `url_clusterNum_flat.txt`
- `url_clusterNum_single.txt`
- `url_clusterNum_avg.txt`
- `cluster_center_flat.txt`
- `cluster_center_single.txt`
- `cluster_center_avg.txt`
