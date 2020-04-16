"""
G是二分图吗?
双色问题
"""


class TwoColor:
    def __init__(self, G):
        """
        Args:
            G: Graph
        """
        self.is_two_colorable = True
        self.marked = [False for _ in range(G.V)]
        self.color = [False for _ in range(G.V)]
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        """
        Args:
            G: Graph
            v: int
        """
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            elif self.color[w] == self.color[v]:
                self.is_two_colorable = False
        