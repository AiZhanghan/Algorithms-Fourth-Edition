from chapter1.Queue import Queue
from chapter1.Stack import Stack


class BreadthFirstPaths:
    def __init__(self, G, s):
        """
        Args:
            G: Graph
            s: int
        """
        # 到达该顶点的最关路径是否已知
        self.marked = [False for _ in range(G.V)]
        # 从起点到一个顶点的已知路径上的最后一个顶点
        # TODO 初始化
        self.edge_to = [x for x in range(G.V)]
        # 起点
        self.s = s
        self.bfs(G, s)
    
    def bfs(self, G, s):
        """
        Args:
            G: Graph
            s: int
        """
        queue = Queue()
        # 标记起点
        self.marked[s] = True
        # 将它加入队列
        queue.enqueue(s)
        while queue:
            # 从队列中删去下一顶点
            v = queue.dequeue()
            for w in G.adj[v]:
                # 对于每一个未标记的相邻结点
                if not self.marked[w]:
                    # 保存最短路径的最后一条边
                    self.edge_to[w] = v
                    # 标记它, 因为最短路径已知
                    self.marked[w] = True
                    # 并将它添加到队列中
                    queue.enqueue(w)

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

    