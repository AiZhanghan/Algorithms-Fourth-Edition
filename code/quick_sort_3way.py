import random
import numpy as np

from is_sorted import is_sorted


def quick_sort_3way(a):
    """三向切分快速排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    random.shuffle(a)
    _sort(a, 0, len(a) - 1)


def _sort(a, lo, hi):
    """
    Args:
        a: list[Item], Item可比较并且重载比较运算符
        lo: int
        hi: int
    """
    if hi <= lo:
        return
    lt = lo
    i = lo + 1
    gt = hi
    v = a[lo]
    while i <= gt:
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    # 现在a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi]成立
    _sort(a, lo, lt - 1)
    _sort(a, gt + 1, hi)