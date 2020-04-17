class MaxPQ:
    """优先队列
    
    Attrs:
        pq, 基于堆的完全二叉树, 存储于pq[1..N]中, pq[0]没有使用
    """

    def __init__(self, a=None):
        """创建一个优先队列
        
        Args:
            a: list[Key], 用a[]中的元素创建一个优先队列
        """
        if a:
            pass
        else:
            self.pq = [None]

    def insert(self, v):
        """向优先队列中插入一个元素
        
        Args:
            v: Key, 可比较类型
        """
        self.pq.append(v)
        self.swim(len(self.pq) - 1)

    def get_max(self):
        """返回最大元素
        
        Return:
            Key
        """
        return self.pq[1]

    def del_max(self):
        """删除并返回最大值
        
        Return:
            Key
        """
        # 从根节点得到最大元素
        max_ = self.pq[1]
        # 将其和最后一个结点交换
        self.pq[1] = self.pq.pop()
        self.sink(1)
        return max_

    def __len__(self):
        """返回优先队列中的元素个数
        
        Return:
            int
        """
        return len(self.pq) - 1
    
    def swim(self, k):
        """上浮
        
        Args:
            k: int
        """
        while k > 1 and self.pq[k // 2] < self.pq[k]:
            self.pq[k // 2], self.pq[k] = self.pq[k], self.pq[k // 2]
            k = k // 2
    
    def sink(self, k):
        """下沉
        
        Args:
            k: int
        """
        while 2 * k < len(self.pq):
            j = 2 * k
            if j < len(self.pq) - 1 and self.pq[j] < self.pq[j + 1]:
                j += 1
            if not self.pq[k] < self.pq[j]:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j