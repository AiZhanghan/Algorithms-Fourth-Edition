from chapter1.Stack import Stack
# from chapter2.IndexMinPQ import IndexMinPQ


class DijkstraSP:
    def __init__(self, G, s):
        """
        Args:
            G: EdgeWeightedDigraph
            s: int
        """
        self.edge_to = [None for _ in range(G.V)]
        self.dist_to = [float("inf") for _ in range(G.V)]
        self.dist_to[s] = 0
        self.pq = IndexMinPQ(G.V)
        self.pq.insert(s, 0.0)
        while self.pq:
            self.relax(G, self.pq.del_min())
        
    def relax(self, G, v):
        """
        Args:
            G: EdgeWeightedDigraph
            v: int
        """
        for e in G.adj[v]:
            w = e.to()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if self.pq.contains(w):
                    self.pq.change(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])

    def has_path_to(self, v):
        """
        Args:
            v: int

        Return:
            bool
        """
        return self.dist_to[v] < float("inf")

    def path_to(self, v):
        """
        Args:
            v: int
        
        Return:
            Iterable<DirectedEdge>
        """
        if not self.has_path_to(v):
            return
        path = Stack()
        e = self.edge_to[v]
        while e:
            path.push(e)
            e = self.edge_to[e.from_()]
        return path
