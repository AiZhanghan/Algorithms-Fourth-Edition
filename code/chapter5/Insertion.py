class Insertion:
    def sort(self, a, lo, hi, d):
        """从第d个字符开始对a[lo]到a[hi]排序

        Args:
            a: list[str]
            lo: int
            hi: int
            d: int
        """
        for i in range(lo, hi + 1):
            j = i
            while j > lo and self.less(a[j], a[j - 1], d):
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
    
    def less(self, v, w, d):
        """
        Args:
            v: str
            w: str
            d: int
        
        Return:
            bool
        """
        return v[d] < w[d]