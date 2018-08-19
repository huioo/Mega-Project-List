# Fibonacci Sequence
"""
 Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

 referer:
 https://github.com/MrBlaise/learnpython/blob/master/Numbers/fibonacci.py
"""


def sequence_length(maximum=100):
    print('Enter the number of lengths of the Fibonacci sequence you want: ')
    while True:
        s = input('>>> ')
        try:
            digits = int(s)
            if digits >= maximum:
                print("Enter a number smaller than %d." % maximum)
            elif digits >= 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("You did not enter an integer")


def fibonacci(n):
    """
    Fibonacci number
        https://en.wikipedia.org/wiki/Fibonacci_number
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    length = sequence_length()
    print('the %dth number:' % length, fibonacci(length))


if __name__ == '__main__':
    main()
