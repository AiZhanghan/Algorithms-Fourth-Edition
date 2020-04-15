from chapter1.Bag import Bag


class Graph:
    def __init__(self, V):
        """
        Args:
            V: int
        """
        # 顶点数目
        self.V = V
        # 边的数目
        self.E = 0
        # 邻接表
        self.adj = [Bag() for _ in range(V)]

    def add_edge(self, v, w):
        """
        Args:
            v: int
            w: int
        """
        # 将w添加到v的链表中
        self.adj[v].add(w)
        # 将v添加到w的链表中
        self.adj[w].add(v)
        self.E += 1

    def __str__(self):
        """图的邻接表的字符串表示, Graph的实例方法

        Return:
            str
        """
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for v in range(self.V):
            s += ("%d: " % v)
            for w in self.adj(v):
                s +=("%d " % w)
            s += "\n"
        return s