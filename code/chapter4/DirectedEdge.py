class DirectedEdge:
    def __init__(self, v, w, weight):
        """
        Args:
            v: int, 边的起点
            w: int, 边的终点
            weight: int, 边的权重
        """
        self.v = v
        self.w = w
        self.weight = weight

    def from_(self):
        """
        Return:
            int
        """
        return self.v

    def to(self):
        """
        Return:
            int
        """
        return self.w

    def __str__(self):
        """
        Return:
            str
        """
        return "%d->%d %.2f" % (self.v, self.w, self.weight)
        