from SequentialSearchST import SequentialSeachST


class SeparateChainingHashST:
    def __init__(self, M=997):
        """创建M条链表
        
        Args:
            M: int
        """
        # 键值对总数
        self.N = 0
        # 散列表的大小
        self.M = M
        # 存放链表对象的数组
        self.st = [SequentialSeachST() for _ in range(M)]

    def _hash(self, key):
        """
        Args:
            key: Key

        Return:
            int
        """
        return abs(hash(key)) % self.M

    def get(self, key):
        """
        Args:
            key: Key
        
        Return:
            Value
        """
        return self.st[self._hash(key)].get(key)

    def put(self, key, val):
        """
        Args:
            key: Key
            val: Value
        """
        self.st[self._hash(key)].put(key, val)
        
    