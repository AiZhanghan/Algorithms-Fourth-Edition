from chapter1.Bag import Bag

class EdgeWeightedDigraph:
    def __init__(self, V):
        """
        Args:
            V: int, 顶点总数
        """
        self.V = V
        # 边的总数
        self.E = 0
        # 邻接表
        self.adj = [Bag() for _ in range(V)]
    
    def add_edge(self, e):
        """
        Args:
            e: DirectedEdge
        """
        self.adj[e.from_()].add(e)
        self.E += 1
    
    def edges(self):
        """
        Return:
            Iterable<DirectedEdge>
        """
        bag = Bag()
        for v in range(self.V):
            for e in self.adj[v]:
                bag.add(e)
        return bag