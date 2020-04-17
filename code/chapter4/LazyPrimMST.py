from chapter2.MinPQ import MinPQ
from chapter1.Queue import Queue


class LazyPrimMST:
    def __init__(self, G):
        """
        Args:
            G: EdgeWeightedGraph
        """
        self.marked = [False for _ in range(G.V)]
        self.pq = MinPQ()
        self.mst = Queue()

        self.visit(G, 0)
        while self.pq:
            # 从pq中得到权重最小的边
            e = self.pq.del_min()

            v = e.either()
            w = e.other(v)
            # 跳过失效的边
            if self.marked[v] and self.marked[w]:
                continue
            # 将边添加到树中
            self.mst.enqueue(e)
            if not self.marked[v]:
                self.visit(G, v)
            if not self.marked[w]:
                self.visit(G, w)

    def visit(self, G, v):
        """标记顶点v并将所有连接v和未标记顶点的边加入pq
        
        Args:
            G: EdgeWeightedGraph
            v: int
        """
        self.marked[v] = True
        for e in G.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        """
        Retuen:
            Iterable<Edge>
        """
        return self.mst
