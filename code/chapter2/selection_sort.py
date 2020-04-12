import numpy as np

from is_sorted import is_sorted


def selection_sort(a):
    """选择排序, 将a按升序排序
    Args:
        a: list[Item], Item可比较并且重载比较运算符
    """
    # 数组长度
    N = len(a)
    for i in range(N):
        # 将a[i]和a[i+1..N]中最小的元素交换
        # 最小元素的索引
        min_ = i
        for j in range(i + 1, N):
            if a[j] < a[min_]:
                min_ = j
        a[i], a[min_] = a[min_], a[i]


if __name__ == "__main__":
    N = 1000
    a = np.random.randint(0, N, size=N)
    print(is_sorted(a))
    selection_sort(a)
    print(is_sorted(a))
