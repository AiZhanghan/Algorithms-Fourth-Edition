class Accumulator:
    def __init__(self):
        self.total = 0
        self.n = 0

    def add_data_value(self, val):
        """添加一个新的数据值

        Args:
            val: float
        """
        self.n += 1
        self.total += val
    
    def mean(self):
        """所有数据的平均值

        Return:
            float
        """
        return self.total / self.n

    def __str__(self):
        """对象的字符串表示

        Return:
            str
        """
        return "Mean (%d values): %7.5f" % (self.n, self.mean())
