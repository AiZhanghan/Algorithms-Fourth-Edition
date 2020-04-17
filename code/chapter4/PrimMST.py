class PrimMst:
    def __init__(self, G):
        """
        Args:
            G: EdgeWeightedEdge
        """
        # 距离树最近的边
        self.edge_to = [None for _ in range(G.V)]
        # dist_to[w] = edge_to[w].weight()
        self.dist_to = [float("inf") for _ in range(G.V)]
        # 如果v在树中则为True
        self.marked = [False for _ in range(G.V)]
        # 有效的横切边
        self.pq = IndexMinPQ()

        self.dist_to[0] = 0.0
        # 用顶点0和权重0初始化pq
        self.pq.insert(0, 0.0)
        while self.pq:
            # 将最近的顶点添加到树中
            self.visit(G, self.pq.del_min())

    def visit(self, G, v):
        """将顶点v添加到树中, 更新数据

        Args:
            G: EdgeWeightedGraph
            v: int
        """
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.other(v)
            # v-w失效
            if self.marked[w]:
                continue
            if e.weight < self.dist_to[w]:
                # 连接w和树的最佳边Edge变成e
                self.edge_to[w] = e
                self.dist_to[w] = e.weight
                if self.pq.contains(w):
                    self.pq.change(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])