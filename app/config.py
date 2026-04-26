from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

SOLR_URL = os.getenv("SOLR_URL", "http://localhost:8983/solr/nutch")
SOLR_CORE = os.getenv("SOLR_CORE", "nutch")
SOLR_ROWS = int(os.getenv("SOLR_ROWS", "200"))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
FLASK_HOST = os.getenv("FLASK_HOST", "127.0.0.1")
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))

PAGERANK_FILE = PROCESSED_DATA_DIR / "r_modified_scores.txt"
HITS_FILE = PROCESSED_DATA_DIR / "hits_scores.txt"
TFIDF_FILE = PROCESSED_DATA_DIR / "tfidfVec.pkl"
URL_CLUSTER_FLAT_FILE = PROCESSED_DATA_DIR / "url_clusterNum_flat.txt"
URL_CLUSTER_SINGLE_FILE = PROCESSED_DATA_DIR / "url_clusterNum_single.txt"
URL_CLUSTER_AVG_FILE = PROCESSED_DATA_DIR / "url_clusterNum_avg.txt"
CENTER_FLAT_FILE = PROCESSED_DATA_DIR / "cluster_center_flat.txt"
CENTER_SINGLE_FILE = PROCESSED_DATA_DIR / "cluster_center_single.txt"
CENTER_AVG_FILE = PROCESSED_DATA_DIR / "cluster_center_avg.txt"
