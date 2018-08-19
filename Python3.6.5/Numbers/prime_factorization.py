# Prime Factorization
"""
 Have the user enter a number and find all Prime Factors (if there are any) and display them.

 素数分解
 素因子分解；质因数连乘式；标准分解式，分解成质数的乘绩
 
 referer:
 https://github.com/geekpradd/Prime-Factorise/blob/master/primefactorize.py
 ** Todo : 完善
 https://github.com/whoshuu/Projects/blob/master/Numbers/prime.py
"""
from random import randint
from fractions import gcd


def get_number(maximum=100):
    print('Enter the number sequence you want to factorize: ')
    while True:
        s = input('>>> ')
        try:
            number = int(s)
            if number >= maximum:
                print("Enter a number smaller than %d." % maximum)
            elif number > 0:
                return number
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("You did not enter an integer")


def prime_factors(num):
    """
    prime_factors: 质因子
    分解质因数: 试除法
    Prime number
        https://en.wikipedia.org/wiki/Prime_number
    Factorization
        https://en.wikipedia.org/wiki/Factorization
    :return:
    """
    return [i for i in range(2, round((num+1)/2)) if 0 == num % i]
    

def prime_factors_ver1(num):
    """
    分解质因数: 试除法
    遍历num所有可能的因子，返回所有实际的因子
    """
    result = []
    for i in range(2, num + 1):
        s = 0
        while num % i == 0:   # 判断是否可以继续整除
            num = num / i
            s += 1
        if s > 0:   # 即可以整除i
            for k in range(s):
                result.append(i)
            if num == 1:
                return result


def prime_factor_by_brent(num):
    """ 实现 Richard Brent's Pollard rho 算法；需要整数本身不是质数。
    
    这个算法不是确定的。有时它会返回输入的复合因子整数 """
    if num % 2 == 0:
        return
    y = randint(1, num - 1)
    c = randint(1, num - 1)
    m = randint(1, num - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y ** 2) % num + c) % num
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % num + c) % num
                q = q * (abs(x - y)) % num
            g = gcd(q, num)
            k = k + m
        r = r * 2
        if g == num:
            while True:
                ys = ((ys * ys) % num + c) % num
                g = gcd(abs(x - ys), num)
                if g > 1:
                    break
    return g


def integer_factors(num):
    """    因子    """
    l = prime_factors(num)
    return [1] + l + [num]


def main():
    number = get_number()
    # print(prime_factors(number))
    # print(integer_factors(number))


if __name__ == '__main__':
    main()
