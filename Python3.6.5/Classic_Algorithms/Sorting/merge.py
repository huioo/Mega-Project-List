# 合并两个有序列表

"""
合并两个有序列表
分解成多个一个元素的列表时，类似归并排序。
https://github.com/taizilongxu/interview_python#8-%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E5%88%97%E8%A1%A8
"""


# 1 尾递归
def _recursion_merge_sort2(l1, l2, tmp):
    """ 递归合并排序
    
    递归对2个列表进行操作，每次取各列表第一个元素插入到传递的中间列表中 """
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


# 循环算法
def loop_merge_sort(l1, l2):
    """
    定义新的空列表存放结果；
    比较2个列表第一个元素，插入小的元素到新列表中，并删除该元素
    最终会出现2个列表中某个列表为空的情况，将旧列表追加到新列表的最后
    """
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


# pop弹出
def merge_sortedlist(a, b):
    c = []
    while a and b:
        if a[0] >= b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c


if __name__ == '__main__':
    l1 = [1, 2, 3, 7]
    l2 = [3, 4, 5]
    print(merge_sortedlist(l1, l2))
