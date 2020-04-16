"""
使用深度优先搜索找出图中的所有连通分量
"""


class CC:
    def __init__(self, G):
        """
        Args:
            G: Graph
        """
        self.marked = [False for _ in range(G.V)]
        self.id = [x for x in range(G.V)]
        self.count = 0
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s)
                self.count += 1

    def dfs(self, G, v):
        """
        Args:
            G: Graph
            v: int
        """
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def is_connected(self, v, w):
        """
        Args:
            v: int
            w: int
        
        Return:
            bool
        """
        return self.id[v] == self.id[w]
