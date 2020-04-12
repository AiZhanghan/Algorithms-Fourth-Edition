class Node:
    """链表结点的定义"""
    def __init__(self, key, val, next):
        """
        Args:
            key: Key
            val: Value
            next: Node
        """
        self.key = key
        self.val = val
        self.next = next


class SequentialSeachST:
    """顺序查找, 基于无序链表"""
    def __init__(self):
        self.first = None

    def get(self, key):
        """查找给定的键, 返回相关联的值

        Args:
            key: Key
        
        Return:
            Value
        """
        x = self.first
        while x:
            # 命中
            if key == x.key:
                return x.val
            x = x.next
        # 未命中
        return None
    
    def put(self, key, val):
        """查找给定的键, 找到则更新其值, 否则在表中新建结点

        Args:
            key: Key
            val: Value
        """
        x = self.first
        while x:
            # 命中, 更新
            if key == x.key:
                x.val = val
                return
            x = x.next
        # 未命中, 新建节点
        self.first = Node(key, val, self.first)