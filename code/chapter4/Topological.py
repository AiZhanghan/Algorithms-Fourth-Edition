from DirectedCycle import DirectedCycle
from DepthFirstOrder import DepthFirstOrder


class Topological:
    def __init__(self, G):
        """
        Args:
            G: Digraph
        """
        self.order = None
        cycle_finder = DirectedCycle(G)
        if not cycle_finder.has_cycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reverse_post
    
    def isDAG(self):
        """
        Return:
            bool
        """
        return self.order != None