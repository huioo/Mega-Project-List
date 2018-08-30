# 杨氏矩阵查找
"""

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

使用Step-wise线性搜索。

"""


def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1  # 行序号
    n = len(l[0]) - 1   # 列序号
    r = 0
    c = n
    while c >= 0 and r <= m:
        # 初始比较每行最右边元素
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            # 往该行左边查找
            c = c - 1
        elif value < x:
            # 往下一行同列查找
            r = r + 1
    return False
