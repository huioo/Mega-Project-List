# Next Prime Number
"""
 Have the program find prime numbers until the user chooses to stop asking for the next one.
 
 让程序找到质数，直到用户选择不再要求下一个。
 
 referer:
 https://github.com/turlapatykaushik/Programs-and-codes/blob/master/problems/prime_number_generator.py
 https://github.com/MrBlaise/learnpython/blob/master/Numbers/next_prime.py
"""


def is_prime(x):
    """ Checks whether the given number x is prime or not """
    if x == 2 and x % 2 != 0:
        return True

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True


def all_prime_numbers(maximum=100):
    start = 1
    while start < maximum:
        # all([]) --> True
        if all(start % i != 0 for i in range(2,  start//2 + 1)):
            print(start)
        start += 1


def main():
    all_prime_numbers()


if __name__ == '__main__':
    main()
