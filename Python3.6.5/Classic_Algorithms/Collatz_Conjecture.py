# Collatz Conjecture
"""
 Start with a number n > 1.
 Find the number of steps it takes to reach one using the following process:
   If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

从一个数字n开始。
通过以下过程找到到达一个步骤所需的步骤：
如果n是偶数，除以2。如果n是奇数，乘以3再加1。

referer:
https://github.com/tiikeri/pythonscripts/blob/master/collatz_conjecture.py
"""
import sys
from time import sleep

is_even = lambda x: not bool(x % 2)
is_odd = lambda x: bool(x % 2)
func = lambda x: x / 2 if is_even(x) else x * 3 + 1


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    
    def __getattr__(self, attr):
        return getattr(self.stream, attr)


def main():
    sys.stdout = Unbuffered(sys.stdout)
    n = 1000
    numbers = []
    # repeat = [4, 2, 4, 2]
    while n != 1:
        print("%s --> " % (str(n)), end='')
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        # print("%s --> " % (str(n)), end='')
        numbers.append(n)
    sleep(0.5)
    return numbers


if __name__ == '__main__':
    # print(func(3))
    main()
