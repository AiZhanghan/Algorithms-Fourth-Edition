class Stack:
    """基于list实现"""
    def __init__(self):
        """创建空栈"""
        self.stack = []

    def push(self, item):
        """添加一个元素
        
        Args:
            item: Item
        """
        self.stack.append(item)

    def pop(self):
        """删除最早添加的元素
        
        Return:
            Item
        """
        return self.stack.pop()

    def __len__(self):
        """栈中的元素数量
        
        Return:
            int
        """
        return len(self.stack)
    
    def __iter__(self):
        """返回一个迭代器"""
        # 记录迭代位置, 从len(self.stack) - 1开始
        self.position = len(self.stack) - 1
        return self

    def __next__(self):
        """返回迭代器下一个指向的值"""
        if self.position >= 0:
            item = self.stack[self.position]
            self.position -= 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    s = Stack()
    while True:
        item = input()
        if item == "q":
            break
        elif s and item == "-":
            print(s.pop())
        else:
            s.push(item)
    print("(%d left in stack)" % len(s))

    for item in s:
        print(item)
