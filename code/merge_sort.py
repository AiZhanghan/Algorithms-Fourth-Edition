import numpy as np

from is_sorted import is_sorted


def merge_sort(a):
    """归并排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    # 归并所需的辅助数组, 一次性分配空间
    aux = [None] * len(a)
    _sort(a, 0, len(a) - 1, aux)


def _sort(a, lo, hi, aux):
    """将数组a[lo..hi]排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
        lo: int
        hi: int
        aux: list[Item], 归并所需的辅助数组
    """
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    # 将左半边排序
    _sort(a, lo, mid, aux)
    # 将右半边排序
    _sort(a, mid + 1, hi, aux)
    # 归并结果
    _merge(a, lo, mid, hi, aux)


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
    merge_sort(a)
    print(is_sorted(a))
