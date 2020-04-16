from chapter1.Stack import Stack


class DepthFirstPaths:
    def __init__(self, G, s):
        """
        Args:
            G: Graph
            s: int
        """
        # 这个顶点上是否调用过dfs()
        self.marked = [False for _ in range(G.V)]
        # 从起点到一个顶点的已知路径上的最后一个顶点
        # TODO 初始化
        self.edge_to = [x for x in range(G.V)]
        # 起点
        self.s = s
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
                self.edge_to[w] = v
                self.dfs(G, w)

    def has_path_to(self, v):
        """
        Args:
            v: int
        
        Return:
            bool
        """
        return self.marked[v]

    def path_to(self, v):
        """
        Args:
            v: int
        
        Return:
            Iterable<int>
        """
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to(x)
        path.push(self.s)
        return path

    