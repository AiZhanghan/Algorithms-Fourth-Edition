"""
G是无环图吗?
假设不存在自环或平行边
"""


class Cycle:
    def __init__(self, G):
        """
        Args:
            G: Graph
        """
        self.marked = [False for _ in range(G.V)]
        self.has_cycle = False
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        """
        Args:
            G: Graph
            v: int
            u: int
        """
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w, v)
            elif w != v:
                self.has_cycle = True