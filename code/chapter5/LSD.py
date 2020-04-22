class LSD:
    """低位优先的字符串排序"""
    
    def sort(self, a, W):
        """通过前W个字符将a[]排序

        Args:
            a: list[str]
            W: int
        """
        N = len(a)
        # ASCII
        R = 128
        aux = [None for _ in range(N)]

        # 根据第d个字符用键索引计数法排序
        for d in range(W - 1, -1, -1):
            # 计算出现频率
            count = [0 for _ in range(R + 1)]
            for i in range(N):
                count[ord(a[i][d]) + 1] += 1
            # 将频率转换为索引
            for r in range(R):
                count[r + 1] += count[r]
            # 将元素分类
            for i in range(N):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] += 1
            # 回写
            for i in range(N):
                a[i] = aux[i]
