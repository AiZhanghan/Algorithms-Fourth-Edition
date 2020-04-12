import time


class Stopwatch:
    """计时器"""
    def __init__(self):
        """创建一个计时器"""
        self.start = time.time()
    
    def elapsed_time(self):
        """返回对象创建以来所经历的时间"""
        now = time.time()
        return now - self.start
    
    def __str__(self):
        return "%f seconds" % self.elapsed_time()


if __name__ == "__main__":
    timer = Stopwatch()
    for _ in range(1000000):
        pass
    print(timer)
            