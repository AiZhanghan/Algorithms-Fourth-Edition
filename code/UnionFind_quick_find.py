class UnionFind:
    def __init__(self, n):
        """以整数标识(0到n - 1)初始化n个触点

        Args:
            n: int
        """
        # 分量id, 以触点作为索引
        self.id = [x for x in range(n)]
        # 分量数量
        self._count = n

    def union(self, p, q):
        """在p和q之间添加一条连接

        Args:
            p: int
            q: int
        """
        # 将p和q归并到相同的分量中
        p_id = self.find(p)
        q_id = self.find(q)

        # 如果p和q已经在相同的分量中则不需要采取任何行动
        if p_id == q_id:
            return

        # 将p的分量重命名为q的名称
        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
        self._count -= 1

    def find(self, p):
        """p(0到n - 1)所在的分量的标识符

        Args:
            p: int
        
        Return:
            int
        """
        return self.id[p]

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
