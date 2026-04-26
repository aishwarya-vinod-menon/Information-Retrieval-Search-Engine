import json
from app.config import PAGERANK_FILE, HITS_FILE


class RankingService:
    def __init__(self) -> None:
        self.page_rank = self._load_scores(PAGERANK_FILE)
        self.hits = self._load_scores(HITS_FILE)

    @staticmethod
    def _load_scores(path):
        if not path.exists():
            return {}
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _normalize_url(result: dict) -> str:
        url = result.get("url", "")
        return url[0] if isinstance(url, list) and url else url

    def apply(self, method: str, results: list[dict]) -> list[dict]:
        if method == "page_rank":
            return sorted(results, key=lambda x: self.page_rank.get(self._normalize_url(x), 0), reverse=True)
        if method == "hits":
            return sorted(results, key=lambda x: self.hits.get(self._normalize_url(x), 0), reverse=True)
        return results
