from archive.legacy.clustering import Clustering


class ClusteringService:
    def __init__(self) -> None:
        self.cluster = Clustering()

    def apply(self, query: str, method: str, results: list[dict]) -> list[dict]:
        if method == "flat_clustering":
            return self.cluster.flat_Clustering(query, results)
        if method == "single_hac":
            return self.cluster.hierarchical_clustering_single(query, results)
        if method == "average_hac":
            return self.cluster.hierarchical_clustering_average(query, results)
        return results
