import heapq


class MinPQ:
    """优先队列, 基于heapq"""

    def __init__(self, a=None):
        """创建一个优先队列

        Args:
            a: list[Key], 用a[]中的元素创建一个优先队列
        """
        if a:
            self.pq = heapq.heapify(a)
        else:
            self.pq = []

    def insert(self, v):
        """向优先队列中插入一个元素
        
        Args:
            v: Key, 可比较类型
        """
        heapq.heappush(self.pq, v)

    def get_min(self):
        """返回最小元素
        
        Return:
            Key
        """
        return self.pq[0]

    def del_min(self):
        """删除并返回最小值
        
        Return:
            Key
        """
        # 从根节点得到最小元素
        return heapq.heappop(self.pq)

    def __len__(self):
        """返回优先队列中的元素个数
        
        Return:
            int
        """
        return len(self.pq)
    