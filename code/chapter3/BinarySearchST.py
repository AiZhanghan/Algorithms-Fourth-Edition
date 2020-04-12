class BinarySearchST:
    """二分查找, 基于有序数组"""
    def __init__(self):
        self.keys = []
        self.vals = []
    
    def __len__(self):
        """
        Return:
            int
        """
        return len(self.keys)
    
    def get(self, key):
        """
        Args:
            key, Key
        
        Return:
            val, Value
        """
        if not self:
            return None
        i = self.rank(key)
        if i < len(self) and self.keys[i] == key:
            return self.vals[i]
        else:
            return None
    
    def rank(self, key):
        """
        Args:
            key: Key

        Return:
            int
        """
        pass

    def put(self, key, val):
        """查找键, 找到则更新值, 否则创建新的元素
        Args:
            key: Key
            val: Value
        """
        i = self.rank(key)
        if i < len(self) and self.keys[i] == key:
            self.vals[i] = val
            return
        self.keys.insert(i, key)
        self.vals.insert(i, val)
