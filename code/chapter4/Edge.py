import functools


@functools.total_ordering
class Edge:
    def __init__(self, v, w, weight):
        """
        Args:
            v: int, 顶点之一
            w: int, 另一个顶点
            weight: float, 边的权重
        """
        self.v = v
        self.w = w
        self.weight = weight
    
    def either(self):
        """
        Return:
            int
        """
        return self.v
    
    def other(self, vertex):
        """
        Args:
            vertex: int
        
        Return:
            int
        """
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise RuntimeError("Inconsistent edge")

    def __lt__(self, that):
        """
        Args:
            that: Edge
        
        Return:
            bool
        """
        return self.weight < that.weight

    def __eq__(self, that):
        """
        Args:
            that: Edge
        
        Return:
            bool
        """
        return self.weight == that.weight

    def __ne__(self, that):
        """
        Args:
            that: Edge
        
        Return:
            bool
        """
        return self.weight != that.weight
    
    def __str__(self):
        """
        Return:
            str
        """
        return "%d-%d %.2f" % (self.v, self.w, self.weight)

