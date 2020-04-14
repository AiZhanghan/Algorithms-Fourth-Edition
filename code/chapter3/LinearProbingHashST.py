class LinearProbingHashST:
    def __init__(self, M=16):
        """
        Args:
            M: int
        """
        # 符号表中键值对的总数
        self.N = 0
        # 线性探测表的大小
        self.M = M
        # 键
        self.keys = [None for _ in range(self.M)]
        # 值
        self.vals = [None for _ in range(self.M)]

    def _hash(self, key):
        """
        Args:
            key: Key

        Return:
            int
        """
        return abs(hash(key)) % self.M

    def resize(self, cap):
        """
        Args:
            cap: int
        """
        t = LinearProbingHashST(cap)
        for i in range(self.M):
            if self.keys[i] != None:
                t.put(self.keys[i], self.vals[i])
        self.keys = t.keys
        self.vals = t.vals
        self.M = t.M

    def put(self, key, val):
        """
        Args:
            key: Key
            val: Value
        """
        # 将M加倍
        if self.N >= self.M / 2:
            self.resize(2 * self.M)
        
        i = self._hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            i = (i + 1) % self.M
        self.keys[i] = key
        self.vals[i] = val
        self.N += 1

    def get(self, key):
        """
        Args:
            key: Key
        
        Return:
            Value
        """
        i = self._hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.M

    def contain(self, key):
        """
        Args:
            key: Key
        
        Return:
            bool
        """
        return self.get(key) != None

    def delete(self, key):
        """
        Args:
            key: Key
        """
        if not self.contain(key):
            return
        i = self._hash(key)
        while key != self.keys[i]:
            i = (i + 1) % self.M
        self.keys[i] = None
        self.vals[i] = None
        i = (i + 1) % self.M
        while self.keys[i] != None:
            key_to_redo = self.keys[i]
            val_to_redo = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.N -= 1
            self.put(key_to_redo, val_to_redo)
            i = (i + 1) % self.M
        self.N -= 1
        if self.N > 0 and self.N == self.M // 8:
            self.resize(self.M // 2)

