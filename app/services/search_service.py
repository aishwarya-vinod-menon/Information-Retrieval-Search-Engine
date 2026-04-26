from app.services.solr_service import SolrService
from app.services.ranking_service import RankingService
from app.services.query_expansion_service import QueryExpansionService
from app.services.clustering_service import ClusteringService
from app.utils.text_preprocessing import preprocess_query


class SearchService:
    def __init__(self) -> None:
        self.solr_service = SolrService()
        self.ranking_service = RankingService()
        self.query_expansion_service = QueryExpansionService()
        self.clustering_service = ClusteringService()

    def run(self, query: str, mode: str) -> dict:
        processed_query = preprocess_query(query)
        solr_query = f'content:"{processed_query}"'
        results = self.solr_service.search(solr_query, apply_randomize=mode not in {"association_qe", "metric_qe", "scalar_qe"})

        results = self.ranking_service.apply(mode, results)
        results = self.clustering_service.apply(processed_query, mode, results)

        final_query = query
        if mode in {"association_qe", "metric_qe", "scalar_qe"}:
            final_query = self.query_expansion_service.expand(mode, processed_query, query, results)
            expanded_solr_query = f'content:"{final_query}"'
            results = self.solr_service.search(expanded_solr_query, apply_randomize=True)

        return {"query": final_query, "query_results": results}
