class Bag:
    """基于list实现"""
    def __init__(self):
        """创建一个空背包"""
        self.bag = []

    def add(self, item):
        """添加一个元素
        
        Args:
            item, Item
        """
        self.bag.append(item)

    def __len__(self):
        """背包中的元素数量
        
        Return:
            int
        """
        return len(self.bag)
    
    def __iter__(self):
        """返回一个迭代器"""
        return iter(self.bag)


# class Bag:
#     """基于set实现, 没有重复元素"""
#     def __init__(self):
#         """创建一个空背包"""
#         self.bag = set()

#     def add(self, item):
#         """添加一个元素
        
#         Args:
#             item, Item
#         """
#         self.bag.add(item)

#     def __len__(self):
#         """背包中的元素数量
        
#         Return:
#             int
#         """
#         return len(self.bag)
    
#     def __iter__(self):
#         """返回一个迭代器"""
#         # 记录迭代位置, 从0开始
#         return iter(self.bag)


if __name__ == "__main__":
    b = Bag()
    while True:
        item = input()
        if item == "q":
            break
        else:
            b.add(item)
    print("(%d left in bag)" % len(b))

    for item in b:
        print(item)
