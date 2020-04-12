import numpy as np

from is_sorted import is_sorted


def shell_sort(a):
    """希尔排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    N = len(a)
    h = 1
    # 1, 4, 13, 40, 121, 364, 1093, ...
    while h < N / 3:
        h = 3 * h + 1
    while h >= 1:
        # 将数组变为h有序
        for i in range(h, N):
            # 将a[i]插入到a[i-h], a[i-2*h], a[i-3*h]...之中
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h = h // 3


if __name__ == "__main__":
    N = 1000
    a = np.random.randint(0, N, size=N)
    print(is_sorted(a))
    shell_sort(a)
    print(is_sorted(a))
