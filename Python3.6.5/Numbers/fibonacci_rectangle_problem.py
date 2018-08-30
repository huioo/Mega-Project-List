# fibonacci rectangle problem

"""

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
  请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    第2*n个矩形的覆盖方法等于第2*(n-1)加上第2*(n-2)的方法。


referer:
https://github.com/huioo/interview_python#3-%E7%9F%A9%E5%BD%A2%E8%A6%86%E7%9B%96


f(n) = f(n-1)+f(n-2)
分别是最后横着放一个矩形的情况为f(n-1)与竖着放2个矩形的情况为f(n-2)

"""

f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)
# f = lambda n: 1 if n < 2 else f(n - 1) + f(1)


if __name__ == '__main__':
    print(f(2), f(3), f(4), f(5))
