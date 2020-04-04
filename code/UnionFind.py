class UnionFind:
    def __init__(self, n):
        """以整数标识(0到n - 1)初始化n个触点

        Args:
            n: int
        """
        # 父链接数组, 以触点作为索引
        self.id = [x for x in range(n)]
        # 由触点索引的各个根节点所对应的分量的大小
        self.sz = [1 for _ in range(n)]
        # 分量数量
        self._count = n

    def union(self, p, q):
        """在p和q之间添加一条连接

        Args:
            p: int
            q: int
        """
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        # 将小树的根节点连接到大树的根节点
        if self.sz[p_root] < self.sz[q_root]:
            self.id[p_root] = self.id[q_root]
            self.sz[q_root] += self.sz[p_root]
        else:
            self.id[q_root] = self.id[p_root]
            self.sz[p_root] += self.sz[q_root]
        self._count -= 1

    def find(self, p):
        """p(0到n - 1)所在的分量的标识符

        Args:
            p: int
        
        Return:
            int
        """
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        """如果p和q存在于同一个分量中则返回True

        Args:
            p: int
            q: int

        Return:
            bool
        """
        return self.find(p) == self.find(q)

    def count(self):
        """连通分量的数量

        Return:
            int
        """
        return self._count
