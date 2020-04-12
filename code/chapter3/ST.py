"""
简单符号表
"""


class ST:
    def __init__(self):
        """创建一张符号表"""
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

    def keys(self):
        """表中的所有键的集合
        
        Return:
            Iterable<Key>
        """
        pass