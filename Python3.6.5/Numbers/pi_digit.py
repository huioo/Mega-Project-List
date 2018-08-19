# Find PI to the Nth Digit
"""
 Enter a number and have the program generate PI up to that many decimal places.
 Keep a limit to how far the program will go.

 输入一个数字，并让程序将PI生成到小数点后的位置。
 限制程序的运行时间。
 
 referer:
 https://github.com/whoshuu/Projects/blob/master/Numbers/pi.py
 https://github.com/geekpradd/PythonPi/blob/master/PythonPi.py
"""
import decimal


def decimal_digits(maximum=10000):
    """
    用户输入，只在给定一个小于10000的非负整数时返回结果
    :return: nonnegative integer 非负整数
    """
    print("How many digits of pi do you want to see? ")
    while True:
        s = input('>>> ')
        try:
            digits = int(s)
            if digits >= maximum:
                print("Enter a number smaller than 10000.")
            elif digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("Enter a nonnegative integer.")


def calc_pi(maxK=1, prec=10, disp=11):
    """
    parameter defaults chosen to gain 1000+ digits within a few seconds
    
    Chudnovsky algorithm :
        https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    
    :param maxK: 迭代次数
    :param prec: precision (for use in rounding, division, square roots..)
    :param disp: 显示小数位数
    :return: π
    """
    decimal.getcontext().prec = prec
    # k=0时，初始值
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK + 1):
        # 参考化简公式计算，k+1值与k值的递归关系
        L += 545140134
        X *= -262537412640768000
        M = (K ** 3 - 16 * K) * M // k ** 3
        
        S += decimal.Decimal(M * L) / X
        K += 12
    C = 426880 * decimal.Decimal(10005).sqrt()
    pi = C / S
    print(pi)
    # drop few digits of precision for accuracy
    pi = decimal.Decimal(str(pi)[:disp])
    print("PI(", " maxK=%d iterations" % maxK,
          " decimal.getcontext().prec=%d" % prec,
          " disp=%d digits" % disp,
          " )",
          " = %s" % pi, sep='\n')
    return pi


def main():
    digits = decimal_digits()
    pi = calc_pi(prec=digits+1, disp=digits+2)


if __name__ == '__main__':
    # main()
    calc_pi()
