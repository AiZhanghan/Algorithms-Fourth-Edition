import numpy as np

from is_sorted import is_sorted


def insertion_sort(a):
    """插入排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    N = len(a)
    for i in range(1, N):
        # 将a[i]插入到a[i-1], a[i-2], a[i-3]...之中
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


if __name__ == "__main__":
    N = 1000
    a = np.random.randint(0, N, size=N)
    print(is_sorted(a))
    insertion_sort(a)
    print(is_sorted(a))
