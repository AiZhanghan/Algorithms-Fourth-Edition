def is_sorted(a):
    """测试数组元素是否有序
    Args:
        a: list[Item]
    Return:
        bool
    """
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True
