from chapter1.Queue import Queue
from chapter1.Stack import Stack
from EdgeWeightedDigraph import EdgeWeightedDigraph


class BellmanFordSP:
    def __init__(self, G: EdgeWeightedDigraph, s: int):
        # 从起点到某个顶点的路径长度
        self.dist_to = [float("inf") for _ in range(G.V)]
        self.dist_to[s] = 0
        # 从起点到某个顶点的最后一条边
        self.edge_to = [None for _ in range(G.V)]
        # 该顶点是否存在于队列中
        self.on_q = [False for _ in range(G.V)]
        # 正在被放松的顶点
        self.queue = Queue()
        # relax()的调用次数
        self.cost = 0
        # edge_to[]中的是否有负权重环
        self.cycle = None

        self.queue.enqueue(s)
        self.on_q[s] = True
        while self.queue and not self.has_negative_cycle():
            v = self.queue.dequeue()
            self.on_q[v] = False
            self.relax(G, v)

    def relax(self, G: EdgeWeightedDigraph, v: int):
        for e in G.adj[v]:
            w = e.to()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if not self.on_q[w]:
                    self.queue.enqueue(w)
                    self.on_q[w] = True
            self.cost += 1
            if self.cost % G.V == 0:
                self.find_negative_cycle()
    
    def has_path_to(self, v: int) -> bool:
        return self.dist_to[v] < float("inf")

    def path_to(self, v: int) -> Stack:
        if not self.has_path_to(v):
            return
        path = Stack()
        e = self.edge_to[v]
        while e:
            path.push(e)
            e = self.edge_to[e.from_()]
        return path

    def find_negative_cycle(self):
        V = len(self.edge_to)
        spt = EdgeWeightedDigraph(V)
        for v in range(V):
            if self.edge_to[v]:
                spt.add_edge(self.edge_to[v])
        
        cf = EdgeWeightedCycleFinder(spt)
        self.cycle = cf.cycle()

    def has_negative_cycle(self) -> bool:
        """是否含有负权重环"""
        return self.cycle != None 

    def negative_cycle(self):
        """得到负权重环, 如果没有则返回None"""
        return self.cycle