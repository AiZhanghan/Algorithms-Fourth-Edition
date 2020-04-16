from DepthFirstOrder import DepthFirstOrder


class kosarajuSCC:
    def __init__(self, G):
        """
        Args:
            G: Digraph
        """
        self.marked = [False for _ in range(G.V)]
        self.id = [x for x in range(G.V)]
        self.count = 0
        order = DepthFirstOrder(G.reverse())
        for s in order.reverse_post:
            if not self.marked[s]:
                self.dfs(G, s)
                self.count += 1
        
    def dfs(self, G, v):
        """
        Args:
            G: Digraph
            v: int
        """
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
    
    def strongly_connected(self, v, w):
        """
        Args:
            v: int
            w: int
        
        Return:
            bool
        """
        return self.id[v] == self.id[w]
