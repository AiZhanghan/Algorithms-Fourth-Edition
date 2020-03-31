def gcd(p, q):
    """计算两个非负整数p和q的最大公约数

    Args:
        p: int
        q: int
    
    Return:
        int
    """
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)
    