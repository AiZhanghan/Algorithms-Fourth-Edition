class DepthFirstSearch:
    def __init__(self, G, s):
        """
        Args:
            G: Graph
            s: int
        """
        self.marked = [False for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)
    
    def dfs(self, G, v):
        """
        Args:
            G: Graph
            v: int
        """
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
    