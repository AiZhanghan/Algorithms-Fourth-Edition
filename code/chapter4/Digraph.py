from chapter1.Bag import Bag


class Digraph:
    def __init__(self, V):
        """
        Args:
            V: int
        """
        self.V = V
        self.E = 0
        self.adj = [Bag() for _ in range(V)]
    
    def add_edge(self, v, w):
        """
        Args:
            v: int
            w: int
        """
        self.adj[v].add(w)
        self.E += 1
    
    def reverse(self):
        """
        Return:
            Digraph
        """
        R = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                R.add_edge(w, v)
        return R