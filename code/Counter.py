class Counter:
    def __init__(self, id_):
        """创建一个名为id的计数器

        Arg:
            id_: str
        """
        self.name = id_
        self.count = 0
    
    def increment(self):
        """将计数器的值加1"""
        self.count += 1
    
    def tally(self):
        """该对象创建后计数器被加1的次数

        Return:
            int
        """
        return self.count
    
    def __str__(self):
        """对象的字符串表示
        
        Return:
            str
        """
        return str(self.count) + " " + self.name


if __name__ == "__main__":
    heads = Counter("heads")
    heads.increment()
    # print(heads + " test")
    print("%s test" % heads)