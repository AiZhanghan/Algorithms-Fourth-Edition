import random
import numpy as np

from is_sorted import is_sorted


def quick_sort(a):
    """快速排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    random.shuffle(a)
    _sort(a, 0, len(a) - 1)


def _sort(a, lo, hi):
    """快速排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
        lo: int
        hi: int
    """
    if hi <= lo:
        return
    # 切分
    j = _partition(a, lo, hi)
    # 将左半部分a[lo..j-1]排序
    _sort(a, lo, j - 1)
    # 将右半部分a[j+1..hi]排序
    _sort(a, j + 1, hi)


def _partition(a, lo, hi):
    """切分, 将数组切分为a[lo..j-1], a[j], a[j+1..hi]
    Args:
        a: list[Item], Item可比较并且重载比较运算符
        lo: int
        hi: int
    """
    # 左右扫描指针
    i = lo
    j = hi + 1
    # 切分元素
    v = a[lo]
    while True:
        # 扫描左右, 检查扫描是否结束并交换元素
        while a[i + 1] < v:
            i += 1
        i += 1
        while v < a[j - 1]:
            j -= 1
        j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    # 将v = a[j]放入正确的位置
    a[lo], a[j] = a[j], a[lo]
    # a[lo..j-1] <= a[j] <= a[j+1..hi]达成
    return j


if __name__ == "__main__":
    N = 1000
    a = np.random.randint(0, N, size=N)
    print(is_sorted(a))
    quick_sort(a)
    print(is_sorted(a))
