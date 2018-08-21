# Merge sort
"""
归并排序

与快速排序思想类似：
 将待排序数据分成两部分，继续将两个子部分进行递归的归并排序；
 然后将已经有序的两个子部分进行合并，最终完成排序。

其时间复杂度与快速排序均为O(nlogn)，但是归并排序除了递归调用间接使用了辅助空间栈，还需要额外的O(n)空间进行临时存储。
从此角度归并排序略逊于快速排序，但是归并排序是一种稳定的排序算法，快速排序则不然。

所谓稳定排序，表示对于具有相同值的多个元素，其间的先后顺序保持不变。
对于基本数据类型而言，一个排序算法是否稳定，影响很小，但是对于结构体数组，稳定排序就十分重要。

referer:
https://github.com/liuyang1/Projects/blob/master/Classic%20Algorithms/mergesort.py
"""
import math


def compare(a, b):
    if a > b:
        return True
    return False


def merge(seq1, seq2):
    ret = []
    while seq1 and seq2:
        if seq1[0] > seq2[0]:
            ret.append(seq2.pop(0))
        else:
            ret.append(seq1.pop(0))
    else:
        # 最后2个数组会出现一个为空数组，一个有一个值且值为最大
        ret.extend(seq1)
        ret.extend(seq2)

    return ret


def merge_sort(iterable):
    length = len(iterable)
    if length <= 1:
        return iterable
    mid = math.ceil(length/2)
    # print('mid:', mid, 'iterable:', iterable)
    # 二路归并排序里面有两个Sort，多路归并排序里面写多个Sort就可以了
    left_l = merge_sort(iterable[:mid])
    right_l = merge_sort(iterable[mid:])
    ret = merge(left_l, right_l)
    
    # print(left_l, right_l, ret)
    return ret


if __name__ == '__main__':
    l = [1, 3, 2, 8, 4, 7, 6, 5]
    # compare_key = lambda x: x
    # print(merge(sorted(l[:4], key=compare_key), sorted(l[4:], key=compare_key)))
    
    print(merge_sort(l))
    print(l)
