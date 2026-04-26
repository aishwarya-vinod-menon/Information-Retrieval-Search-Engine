from archive.legacy import QE


class QueryExpansionService:
    def expand(self, method: str, processed_query: str, original_query: str, results: list[dict]) -> str:
        if method == "association_qe":
            expanded = original_query + QE.association_main(processed_query, results[:30], 3, 10)
        elif method == "metric_qe":
            expanded = QE.metric_cluster_main(processed_query, results[:30])
        elif method == "scalar_qe":
            expanded = QE.scalar_main(processed_query, results[:30])
        else:
            return original_query

        words = list(dict.fromkeys(" ".join(expanded.split()).split()))
        return " ".join(words)
