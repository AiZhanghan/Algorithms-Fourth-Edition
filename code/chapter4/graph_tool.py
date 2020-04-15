"""
常用图处理代码
"""


def degree(G, v):
    """计算v的度数

    Args:
        G: Graph
        v: int
    
    Return:
        int
    """
    res = 0
    for _ in G.adj[v]:
        res += 1
    return res


def max_degree(G):
    """计算所有顶点的最大度数

    Args:
        G: Graph
    
    Return:
        int
    """
    res = 0
    for v in range(G.V):
        if degree(G, v) > res:
            res = degree(G, v)
    return res

def avg_degree(G):
    """计算所有顶点的平均度数

    Args:
        G: Graph
    
    Return:
        int
    """
    return 2 * G.E / G.V

def number_of_self_loops(G):
    """计算自环的个数

    Args:
        G: Graph

    Return:
        int
    """
    count = 0
    for v in range(G.V):
        for w in G.adj[v]:
            if v == w:
                count += 1
    # 每条边都被记过两次? TODO 
    return count // 2
