class DirectedDFS:
    def __init__(self, G, sources):
        """
        Args:
            G: Digraph
            sources: int or list[int]
        """
        if type(sources) == int:
            sources = list(sources)
        self.marked = [False for _ in range(G.V)]
        for s in sources:
            if not self.marked[s]:
                self.dfs(G, s)
        
    def dfs(self, G, v):
        """
        Args:
            G: Digraph
            v: int
        """
        self.marked[v] = True
        for w in G.adj[v]:
            self.dfs(G, w)
            