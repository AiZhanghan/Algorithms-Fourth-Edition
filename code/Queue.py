from collections import deque


class Queue:
    """基于collections.deque"""
    def __init__(self):
        """创建空队列"""
        self.queue = deque()

    def enqueue(self, item):
        """添加一个元素
        
        Args:
            item: Item
        """
        self.queue.append(item)

    def dequeue(self):
        """删除最早添加的元素
        
        Return:
            Item
        """
        return self.queue.popleft()

    def __len__(self):
        """队列中的元素数量
        
        Return:
            int
        """
        return len(self.queue)

    def __iter__(self):
        """返回一个迭代器"""
        # 记录迭代位置, 从0开始
        self.position = 0
        return self

    def __next__(self):
        """返回迭代器下一个指向的值"""
        if self.position < len(self.queue):
            item = self.queue[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    q = Queue()
    while True:
        item = input()
        if item == "q":
            break
        elif q and item == "-":
            print(q.dequeue())
        else:
            q.enqueue(item)
    print("(%d left in queue)" % len(q))

    for item in q:
        print(item)
