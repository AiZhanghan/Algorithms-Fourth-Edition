RED = True
BLACK = False


class Node:
    def __init__(self, key, val, N, color):
        """
        Args:
            key: Key
            val: Value
            N: int
            color: bool
        """
        # 键
        self.key = key
        # 相关联的值
        self.val = val
        # 左右子树
        self.left = None
        self.right = None
        # 这颗子树中的节点总数
        self.N = N
        # 由其父节点指向它的链接的颜色
        self.color = color


class RedBlackBST:
    def __init__(self):
        self.root = None

    def is_red(self, x):
        """
        Args:
            x: Node
        
        Return:
            bool
        """
        if not x:
            return False
        return x.color == RED
    
    def rotate_left(self, h):
        """
        Args:
            h: Node
        
        Return:
            Node
        """
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return x

    def rotate_right(self, h):
        """
        Args:
            h: Node
        
        Return:
            Node
        """
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return x

    def flip_colors(self, h):
        """
        Args:
            h: Node

        Return:
            Node
        """
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

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

    def put(self, key, val):
        """查找key, 找到则更新其值, 否则为它新建一个节点

        Args:
            key: Key
            val: Value
        """
        self.root = self._put(self.root, key, val)
        self.root.color = BLACK
    
    def _put(self, h, key, val):
        """
        Args:
            h: Node
            key: Key
            val: Value
        
        Return:
            Node
        """
        # 标准的插入操作, 和父节点用红链接相连
        if not h:
            return Node(key, val, 1, RED)
        
        if key < h.key:
            h.left = self._put(h.left, key, val)
        elif key > h.key:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val
        
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        
        h.N = self.size(h.left) + self.size(h.right) + 1
        return h