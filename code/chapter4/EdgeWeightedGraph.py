from chapter1.Bag import Bag


class EdgeWeightedGraph:
    def __init__(self, V):
        """
        Args:
            V: int, 顶点总数
        """
        self.V = V
        self.E = 0
        self.adj = [Bag() for _ in range(V)]

    def add_edge(self, e):
        """
        Args:
            e: Edge
        """
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def edges(self):
        """
        Return:
            Iterable<Edge>
        """
        b = Bag()
        for v in range(self.V):
            for e in self.adj[v]:
                if e.other(v) > v:
                    b.add(e)
        return b                    