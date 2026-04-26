from urllib.parse import urlparse
import random
from pysolr import Solr
from app.config import SOLR_URL, SOLR_ROWS


class SolrService:
    def __init__(self) -> None:
        self.solr = Solr(SOLR_URL, always_commit=True)

    @staticmethod
    def _get_domain(url: str) -> str:
        return urlparse(url).netloc

    @staticmethod
    def _randomize(results: list[dict]) -> list[dict]:
        batch_size = 10
        reshuffled = results[:2]
        for idx in range(2, len(results), batch_size):
            chunk = results[idx : idx + batch_size]
            random.shuffle(chunk)
            reshuffled.extend(chunk)
        return reshuffled

    def _filter_by_domain(self, results: list[dict]) -> list[dict]:
        new_results, domain_counts, seen_urls = [], {}, set()
        for result in results:
            url = result.get("url", "")
            if not url or url in seen_urls:
                continue
            domain = self._get_domain(url if isinstance(url, str) else url[0])
            if domain_counts.get(domain, 0) < 4:
                new_results.append(result)
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
            seen_urls.add(url)
        return new_results

    def search(self, query: str, apply_randomize: bool = True) -> list[dict]:
        num_rows = SOLR_ROWS
        curr_count = 0
        solr_results: list[dict] = []

        while curr_count < 50:
            response = self.solr.search(query, search_handler="/select", **{"wt": "json", "rows": num_rows})
            solr_results = [doc for doc in response]
            if len(solr_results) < 50 and ":" in query:
                terms = query.split(":", 1)[1].replace('"', "").split()
                and_q = " AND ".join([f"text:{term}" for term in terms])
                or_q = " OR ".join([f"text:{term}" for term in terms])
                and_resp = self.solr.search(and_q, search_handler="/select", **{"wt": "json", "rows": num_rows})
                or_resp = self.solr.search(or_q, search_handler="/select", **{"wt": "json", "rows": num_rows})
                solr_results.extend([doc for doc in and_resp])
                solr_results.extend([doc for doc in or_resp])

            solr_results = self._filter_by_domain(solr_results)
            curr_count = len(solr_results)
            num_rows *= 2
            if num_rows > 10000:
                break

        return self._randomize(solr_results) if apply_randomize else solr_results
