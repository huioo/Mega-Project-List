# Fibonacci step problem
"""
1 台阶问题/斐波那契
 
 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
 
 referer:
 https://github.com/huioo/interview_python#1-%E5%8F%B0%E9%98%B6%E9%97%AE%E9%A2%98%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91
 
"""

n_steps = 100


def solution1(n):
    if n <= 2:
        return n
    return solution1(n-1) + solution1(n-2)


def memo(func):
    """ 记忆方法
    缓存结果 """
    cache = {}
    
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def solution2(i):
    if i < 2:
        return 1
    return solution2(i-1) + solution2(i-2)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


"""
2 变态台阶问题

 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

 f(n)=1+f(1)+f(2)+...+f(n-1)
 f(n-1)=1+f(1)+f(2)+...+f(n-2)
 f(n)-f(n-1)=f(n-1)
 f(n)=f(n-1) + f(n-1)= 2*f(n-1)

 n=4时，分类如下：
[1,1,1,1]
[1,2,1]
[2,1,1]
[3,1]

[1,1,2]
[2,2]

[1,3]

[4]


"""
fib = lambda n: n if n < 2 else (2 * fib(n - 1))


def fib1(n):
    if n < 2:
        return n
    return 2*fib1(n-1)


from functools import reduce
fib2 = lambda n: n if n < 2 else (1 + reduce(lambda x, y: x+y, [fib(n-i) for i in range(1, n)]))


if __name__ == '__main__':
    print(fib(6), fib1(6), fib2(6))



