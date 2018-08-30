# 快速排序
"""

https://en.wikipedia.org/wiki/Quicksort
"""


def quicksort(l):
    if len(l) < 2:
        return l
    else:
        mid_pivot = l[0]
        lt_mid_pivot = [i for i in l if i < mid_pivot]
        gt_mid_pivot = [i for i in l if i > mid_pivot]
        et_mid_pivot = [i for i in l if i == mid_pivot]
        result = quicksort(lt_mid_pivot) + et_mid_pivot + quicksort(gt_mid_pivot)
        return result


def lomuto_partition_scheme(A, lo, hi):
    """
    i与j开始相等，如果A[j]一直小于A[hi]，则i与j相等，
      否则i不变，下一个j=i+1，若此时A[j]小于A[hi]，则替换A[i]与A[j]
      找到下一个A[j]小于A[hi]时，替换A[i]与A[j]
        (找到第一位大于pivot的元素，与其之后第一个小于pivot的元素进行交换，
        i用来记录需要替换的大于pivot的位置，j标记当前第几位元素，并在A[j]小于pivot时，2个元素进行交换)
    保证i元素之前的所有元素都小于A[hi]即pivot，i元素之后的所有元素都大于等于pivot
    最后在替换A[i]与A[hi]
    """
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        # print(A, i, j, A[i], A[j])
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    print(A, A[i], A[hi])
    return i


def lomuto_quick_sort(A, lo, hi):
    if lo < hi:
        p = lomuto_partition_scheme(A, lo, hi)
        # 第p个元素为pivot，绝对大于前面的所有元素，小于后面的所有元素
        lomuto_quick_sort(A, lo, p-1)
        lomuto_quick_sort(A, p + 1, hi)


def hoare_partition_scheme(A, lo, hi):
    """
    从前向后找大于pivot的元素下标 i，从后往前找小于pivot的元素下标 j，交换2个位置的元素
    在i >= j的时候结束，这时前后替换完全直接返回j，不返回i的原因是由于第i个元素是大于pivot的
    确保大于pivot的元素在后面，小于pivot的元素在前面
    """
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i = i + 1
        while A[i] < pivot:
            i = i + 1
    
        j = j - 1
        while A[j] > pivot:
            j = j - 1
    
        if i >= j:
            print(A, i, j, A[i], A[j])
            return j
    
        A[i], A[j] = A[j], A[i]


def hoare_quick_sort(A, lo, hi):
    if lo < hi:
        p = hoare_partition_scheme(A, lo, hi)
        hoare_quick_sort(A, lo, p)
        hoare_quick_sort(A, p + 1, hi)


if __name__ == '__main__':
    print(hoare_quick_sort([2, 4, 6, 3, 1, 7, 2, 8, 5], 0, 8))
    print(lomuto_quick_sort([2, 4, 6, 3, 1, 7, 2, 8, 5], 0, 8))
