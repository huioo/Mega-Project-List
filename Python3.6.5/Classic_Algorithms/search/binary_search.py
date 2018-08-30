# 二分查找


def binary_search(l, item, counter=1):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        print(counter, 'low', low, 'high', high, 'mid', mid, 'guess', guess)
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
        counter += 1
    return None


mylist = [1, 2, 3, 5, 6, 7, 9]
print('结果', binary_search(mylist, 10))
print('结果', binary_search(mylist, 5))
