from chapter1.Queue import Queue


class Node:
        def __init__(self, key, val, N):
            """
            Args:
                key: Key
                val: Value
                val: int
            """
            # 键
            self.key = key
            # 值
            self.val = val
            # 指向子树的链接
            self.left = None
            self.right = None
            # 以该节点为根的子树中的节点总数
            self.N = N


class BST:
    def __init__(self):
        # 二叉查找树的根节点
        self.root = None

    def __len__(self):
        """
        Return:
            int
        """
        return self.size(self.root)

    def size(self, x):
        """
        Args:
            x: Node

        Return:
            int
        """
        if not x:
            return 0
        else:
            return x.N

    def get(self, key):
        """
        Args:
            key: Key
        
        Return:
            Value
        """
        return self._get(self.root, key)
    
    def _get(self, x, key):
        """在以x为根节点的子树中查找并返回key所对应的值

        Args:
            x: Node
            key: Key
        
        Return:
            Value
        """
        # 如果找不到则返回None
        if not x:
            return
        if key < x.key:
            self._get(x.left, key)
        elif key > x.key:
            self._get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        """查找key, 找到则更新它的值, 否则为它创建一个新的结点
        
        Args:
            key: Key
            val: Value
        """
        self.root = self._put(self.root, key, val)
    
    def _put(self, x, key, val):
        """如果key存在于以x为根节点的子树中则更行它的值;
        否认将以key和val为键值对的新节点插入到该子树中

        Args:
            x: Node
            key: Key
            val: Value
        
        Return:
            Node
        """
        if not x:
            return Node(key, val, 1)
        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.N = self.size(x.left) + self.size(x.right) + 1
        return x

    def min(self):
        """
        Return:
            key: Key
        """
        return self._min(self.root).key
    
    def _min(self, x):
        """
        Args:
            x: Node
        
        Return:
            Node
        """
        if not x.left:
            return x
        return self._min(x.left)
    
    def max(self):
        """
        Return:
            Key
        """
        return self._max(self.root).key

    def _max(self, x):
        """
        Args:
            x: Node

        Return:
            Node
        """
        if not x.right:
            return x
        return self._max(x.right)

    def floor(self, key):
        """
        Args:
            key: Key
        
        Return:
            Key
        """
        x = self._floor(self.root, key)
        if not x:
            return
        return x.key
    
    def _floor(self, x, key):
        """
        Args:
            x: Node
            key: Key
        
        Return:
            Node
        """
        if not x:
            return
        if key == x.key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t:
            return t
        else:
            return x

    def select(self, k):
        """
        Args:
            k: int
        
        Return:
            Key
        """
        return self._select(self.root, k).key
    
    def _select(self, x, k):
        """返回排名为k的结点

        Args:
            x: Node
            k: int
        
        Return:
            Node
        """
        if not x:
            return None
        t = self.size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t < k:
            return self._select(x.right, k - t - 1)
        else:
            return x

    def rank(self, key):
        """
        Args:
            key: Key
        
        Return:
            int
        """
        return self._rank(key, self.root)

    def _rank(self, key, x):
        """返回以x为根节点的子树中小于x.key的键的数量

        Args:
            key: Key
            x: Node

        Return:
            int
        """
        if not x:
            return 0
        if key < x.key:
            return self._rank(key, x.left)
        elif key > x.key:
            return 1 + self.size(x.left) + self._rank(key, x.right)
        else:
            return self.size(x.left)

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, x):
        """
        Args:
            x: Node
        
        Return:
            Node
        """
        if not x.left:
            return x.right
        x.left = self._delete_min(x.left)
        x.N = self.size(x.left) + self.size(x.right) + 1
        return x

    def delete(self, key):
        """
        Args:
            key: Key
        """
        self.root = self._delete(self.root, key)
    
    def _delete(self, x, key):
        """
        Args:
            x: Node
            key: Key
        
        Return:
            Node
        """
        if not x:
            return
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if not x.right:
                return x.left
            if not x.left:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        x.N = self.size(x.left) + self.size(x.right) + 1
        return x

    def keys(self, lo=None, hi=None):
        """
        Args:
            lo: key
            hi: key
        
        Return:
            Iterable<key>
        """
        if not lo:
            lo = self.min()
        if not hi:
            hi = self.max()
        queue = Queue()
        self._keys(self.root, queue, lo, hi)
        return queue

    def _keys(self, x, queue, lo, hi):
        """
        Args:
            x: Node
            queue: Queue<Key>
            lo: Key
            hi: Key
        """
        if not x:
            return
        if lo < x.key:
            self._keys(x.left, queue, lo, hi)
        if lo <= x.key and hi >= x.key:
            queue.enqueue(x.key)
        if hi > x.key:
            self._keys(x.right, queue, lo, hi)




if __name__ == "__main__":
    bst = BST()
    print(len(bst))