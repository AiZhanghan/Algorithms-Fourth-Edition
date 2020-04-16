from Graph import Graph


class SymbolGraph:
    def __init__(self, stream, sp):
        """
        Args:
            stream: str
            sp: str
        """
        # 符号名 -> 索引
        self.st = {}
        # 第一遍
        with open(stream) as f:
            # 构造索引
            for line in f:
                # 读取字符串
                a = line.split(sp)
                # 为每个不同的字符串关联一个索引
                for i in range(len(a)):
                    if a[i] not in self.st:
                        self.st[a[i]] = len(self.st)
        # 用来获得顶点名的反向索引是一个数组
        self.keys = [None for _ in range(len(self.st))]

        for name in self.st.keys():
            self.keys[self.st[name]] = name
        
        self.G = Graph(len(self.st))
        # 第二遍
        with open(stream) as f:
            # 构造图
            for line in f:
                # 将第一行的第一个顶点和该行的其他顶点相连
                a = line.split(sp)
                v = self.st[a[0]]
                for i in range(1, len(a)):
                    self.G.add_edge(v, self.st[a[i]])

    def contains(self, s):
        """
        Args:
            s: str

        Return:
            bool
        """
        return s in self.st

    def index(self, s):
        """
        Args:
            s: str

        Return:
            int
        """
        return self.st[s]
    
    def name(self, v):
        """
        Args:
            v: int

        Return:
            str
        """
        return self.keys[v]
    