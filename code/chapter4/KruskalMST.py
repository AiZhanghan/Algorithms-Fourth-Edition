from chapter1.Queue import Queue
from chapter2.MinPQ import MinPQ
from chapter1.UnionFind import UnionFind


class KruskalMST:
    def __init__(self, G):
        """
        Args:
            G: EdgeWeightedGraph
        """
        self.mst = Queue()
        pq = MinPQ()
        for e in G.edges():
            pq.insert(e)
        uf = UnionFind(G.V)

        while pq and len(self.mst) < G.V:
            # 从pq得到权重最小的边和它的顶点
            e = pq.del_min()
            v = e.either()
            w = e.other(v)
            # 忽略失效的边
            if uf.connected(v, w):
                continue
            # 合并分量
            uf.union(v, w)
            # 将边添加到最小生成树中
            self.mst.enqueue(e)
    def edges(self):
        """
        Return:
            Iterable<Edge>
        """
        return self.mst
