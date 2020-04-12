"""
有序符号表(键有序)
"""


class OrderedST:
    def __init__(self):
        """创建一张有序符号表"""
        pass

    def put(self, key, val):
        """将键值对存入表中, 若值为空则将键key从表中删除
        
        Args:
            key: Key
            val: Value
        
        Return:
            Value
        """
        if not val:
            self.delete(key)
            return
        pass

    def get(self, key):
        """获取键key对应的值, 若键key不存在则返回None
        
        Args:
            key: Key
        
        Return:
            Value
        """
        pass

    def delete(self, key):
        """从表中删去键key
        
        Args:
            key: Key
        """
        self.put(key, None)
        pass

    def contains(self, key):
        """键key在表中是否有对应的值
        
        Args:
            key: Key
        
        Return:
            bool
        """
        return self.get(key) != None

    def __len__(self):
        """表中键值对的数量
        
        Return:
            int
        """
        pass

    def min(self):
        """最小的键
        
        Return:
            Key
        """
        pass

    def max(self):
        """最大的键
        
        Return:
            Key
        """
        pass

    def floor(self, key):
        """小于等于key的最大键
        
        Args:
            key, Key
        
        Return:
            Key
        """
        pass

    def ceiling(self, key):
        """大于等于key的最小键
        
        Args:
            key, Key
        
        Return:
            Key
        """
        pass

    def rank(self, key):
        """小于key的键的数量
        
        Args:
            key, Key
        
        Return:
            int
        """
        pass

    def select(self, k):
        """排名为k的键
        
        Args:
            k, int
        
        Return:
            Key
        """
        pass

    def delete_min(self):
        """删除最小的键"""
        self.delete(self.min())

    def delete_max(self):
        """删除最大的键"""
        self.delete(self.max())

    def size(self, lo, hi):
        """[lo..hi]之间键的数量
        
        Args:
            lo, Key
            hi, Key
        
        Return: 
            int
        """
        if hi < lo:
            return 0
        elif self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def keys(self, lo=None, hi=None):
        """表中的所有键的集合或者[lo..hi]之间的所有键, 已排序
        
        Args:
            lo, Key
            hi, Key
        
        Return:
            Iterable<Key>
        """
        if not lo and not hi:
            return self.keys(self.min(), self.max())
        pass