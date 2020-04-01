def binary_search(key, a):
    """二分查找
    
    Arg:
        key: 待查找元素
        a: 有序数组
    
    Return:
        int: key在数组a中的下标索引, 
            -1表示key不在数组a中
    """
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        # 被查找的键要么不存在, 要么必然存在于a[lo..hi]之中
        mid = lo + (hi - lo) // 2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
