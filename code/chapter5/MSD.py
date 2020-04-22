from Insertion import Insertion


class MSD:
    """高位优先的字符串排序"""
    
    def __init__(self):
        # 基数
        self.R = 128
        # 小数组的切换阈值
        self.M = 15
        # 数据分类的辅助数组
        self.aux = None

    def char_at(self, s, d):
        """根据索引访问字符

        Args:
            s: str
            d: int
        
        Return:
            int
        """
        if d < len(s):
            return ord(s[d])
        else:
            return -1

    def sort(self, a):
        """将a[]排序

        Args:
            a: list[str]
        """
        self.N = len(a)
        self.aux = [None for _ in range(self.N)]
        self._sort(a, 0, self.N - 1, 0)
    
    def _sort(self, a, lo, hi, d):
        """以第d个字符为键将a[lo]至a[hi]paixu

        Args:
            a: list[str]
            lo: int
            hi: int
            d: int
        """
        if hi <= lo + self.M:
            Insertion().sort(a, lo, hi, d)
            return
        # 计算出现频率
        count = [0 for _ in range(self.R + 2)]
        for i in range(lo, hi + 1):
            count[self.char_at(a[i], d) + 2] += 1
        # 将频率转换为索引
        for r in range(self.R + 1):
            count[r + 1] += count[r]
        # 将元素分类
        for i in range(lo, hi + 1):
            self.aux[count[self.char_at(a[i], d) + 1]] = a[i]
            count[self.char_at(a[i], d) + 1] += 1
        # 回写
        for i in range(lo, hi + 1):
            a[i] = self.aux[i - lo]
        
        # 递归的以每个字符为键进行排序
        for r in range(self.R):
            self._sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1)
