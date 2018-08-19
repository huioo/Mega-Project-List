# Find e to the Nth Digit
"""
 Just like the previous problem, but with e instead of PI.
 Enter a number and have the program generate e up to that many decimal places.
 Keep a limit to how far the program will go.

 就像前面的问题一样，但是用e代替PI。
 输入一个数字，让程序生成e的小数点。
 限制程序的运行时间。
 
 referer:
 https://github.com/rlingineni/PythonPractice/blob/master/eCalc/eCalculate.py
 https://github.com/microice333/Python-projects/blob/master/n_digit_e.py

"""
import decimal


def decimal_digits(maximum=1000):
    print('Enter the number of digits you want after the decimal for e: ')
    while True:
        s = input('>>> ')
        try:
            digits = int(s)
            if digits >= maximum:
                print("Enter a number smaller than %d." % maximum)
            elif digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("You did not enter an integer")


def factorial(n):
    """ 阶乘 """
    if n < 1:
        return 1
    return factorial(n-1) * n


def factorials(n):
    """ 阶乘列表 """
    l = [1]
    for i in range(1, n+1):
        l.append(l[i-1]*i)
    return l


def calc_e(n=1000, prec=10, disp=11):
    """
    e (mathematical constant):
        https://en.wikipedia.org/wiki/E_(mathematical_constant)
    :return:
    """
    decimal.getcontext().prec = prec
    l = factorials(n)
    e = 0
    for i in l:
        e += 1 / decimal.Decimal(i)
    e = decimal.Decimal(str(e)[:disp])
    print("E(", " n=%d ———— length of the factorial" % n,
          " decimal.getcontext().prec=%d" % prec,
          " disp=%d digits" % disp,
          " )",
          " = %s" % e, sep='\n')


def main():
    digits = decimal_digits()
    e = calc_e(prec=digits+1, disp=digits+2)


if __name__ == '__main__':
    # main()
    calc_e()
    # print(factorials(5))

