from chapter1.Stack import Stack


class DirectedCycle:
    def __init__(self, G):
        """
        Args:
            G: Digraph
        """
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [x for x in range(G.V)]
        # 有向环中的所有顶点, 如果存在的话
        self.cycle = None
        # 递归调用的栈上的所有顶点
        self.on_stack = [False for _ in range(G.V)]
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)
    
    def dfs(self, G, v):
        """
        Args:
            G: Digraph
            v: int
        """
        self.on_stack[v] = True
        self.marked[v] = True
        for w in G.adj[v]:
            if self.has_cycle():
                return
            elif not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                self.cycle = Stack()
                x = v
                while x != w:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(w)
                self.cycle.push(v)
        self.on_stack[v] = False

    def has_cycle(self):
        """
        Return:
            bool
        """
        return self.cycle != None