from chapter1.Queue import Queue
from chapter1.Stack import Stack

class DepthFirstOrder:
    def __init__(self, G):
        """
        Args:
            G: Digraph
        """
        self.marked = [False for _ in range(G.V)]
        # 所有顶点的前序排序
        self.pre = Queue()
        # 所有顶点的后序排列
        self.post = Queue()
        # 所有顶点的逆后序排列
        self.reverse_post = Stack()

        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        """
        Args:
            G: Digraph
            v: int
        """
        self.pre.enqueue(v)

        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
                
        self.post.enqueue(v)
        self.reverse_post.push(v)
    
    