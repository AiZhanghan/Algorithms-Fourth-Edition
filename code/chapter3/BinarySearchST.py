import sys
sys.path.append("..")
import chapter1


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
        lo = 0
        hi = len(self) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

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
    
    def min(self):
        """
        Return
            key: Key
        """
        return self.keys[0]
    
    def max(self):
        """
        Return:
            key: Key
        """
        return self.keys[-1]
    
    def select(self, k):
        """
        Args:
            k: int
        
        Return:
            key: Key
        """
        return self.keys[k]
    
    def ceiling(self, key):
        """
        Args:
            key: Key
        
        Return:
            Key
        """
        i = self.rank(key)
        return self.keys[i]

    def get_keys(self, lo, hi):
        """
        Args:
            lo, Key
            hi, Key
        
        Return:
            Iterable<Key>
        """
        q = chapter1.Queue.Queue()
        for i in range(self.rank(lo), self.rank(hi)):
            q.enqueue(self.keys[i])
        if self.contains(hi):
            q.enqueue(self.keys[self.rank(hi)])
        return q
    
    def contains(self, key):
        """键key在表中是否有对应的值
        
        Args:
            key: Key
        
        Return:
            bool
        """
        return self.get(key) != None


if __name__ == "__main__":
    table = BinarySearchST()
    table.put("S", 0)
    table.put("E", 1)
    table.put("R", 3)
    table.put("A", 2)
    table.put("A", 8)
    print(len(table))
    print(table.keys)
    print(table.vals)