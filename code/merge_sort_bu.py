import numpy as np

from is_sorted import is_sorted


def merge_sort_bu(a):
    """归并排序, 将a按升序排序, 自底向上
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    # 归并所需的辅助数组, 一次性分配空间
    aux = [None] * len(a)
    # 进行lgN次两两归并
    N = len(a)
    # sz: 子数组大小
    sz = 1
    while sz < N:
        # lo: 子数字索引
        lo = 0
        while lo < N - sz:
            _merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, N - 1), aux)
            lo += sz + sz
        sz = sz + sz


def _merge(a, lo, mid, hi, aux):
    """将a[lo..mid]和a[mid+1..hi]归并
    Args:
        a: list[Item], Item可比较并且重载比较运算符
        lo: int
        mid: int
        hi: int
        aux: list[Item], 归并所需的辅助数组
    """
    i = lo
    j = mid + 1
    
    # 将a[lo..hi]复制到aux[lo..hi]
    for k in range(lo, hi + 1):
        aux[k] = a[k]
    
    # 归并回到a[lo..hi]
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


if __name__ == "__main__":
    N = 1000
    a = np.random.randint(0, N, size=N)
    print(is_sorted(a))
    merge_sort_bu(a)
    print(is_sorted(a))
