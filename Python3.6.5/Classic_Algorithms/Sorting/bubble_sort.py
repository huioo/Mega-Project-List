# bubble sorting
"""
冒泡排序
https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin

referer:
https://github.com/liuyang1/Projects/blob/master/Classic%20Algorithms/mergesort.py
"""


def compare(a, b):
    if a > b:
        return b, a
    return a, b


def my_sort_normal(iterable):
    length = len(iterable)
    for i in range(1, length):
        for _ in range(length - i):
            iterable[_], iterable[_ + 1] = compare(iterable[_], iterable[_ + 1])
            print(i, _, iterable)


def my_sort(iterable):
    length = len(iterable)
    for i in range(1, len(iterable)):
        end = 0
        for _ in range(length-i):
            if iterable[_] > iterable[_+1]:
                iterable[_], iterable[_+1] = iterable[_+1], iterable[_]
                end += 1
            print(i, _, iterable)
        if end == 0:
            break


if __name__ == '__main__':
    l = [8, 3, 2, 1, 4, 7, 6, 5]
    my_sort_normal(l)
    my_sort(l)
    # print(l)


