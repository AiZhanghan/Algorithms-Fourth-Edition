from DirectedDFS import DirectedDFS


class TransitiveClosure:
    def __init__(self, G):
        """
        Args:
            G: Digraph
        """
        self.all = [DirectedDFS(G, v) for v in range(G.V)]
    
    def reachable(self, v, w):
        """
        Args:
            v: int
            w: int
        
        Return:
            bool
        """
        return self.all[v].marked[w]