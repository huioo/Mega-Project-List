# Prime Factorization
"""
 Have the user enter a number and find all Prime Factors (if there are any) and display them.

 素数分解
 素因子分解；质因数连乘式；标准分解式，分解成质数的乘绩
 
 referer:
 https://github.com/geekpradd/Prime-Factorise/blob/master/primefactorize.py
"""


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


def is_prime(num):
    """
    分解质因数: 试除法
    Prime number
        https://en.wikipedia.org/wiki/Prime_number
    Factorization
        https://en.wikipedia.org/wiki/Factorization
    :return:
    """
    return [i for i in range(2, round((num+1)/2)) if 0 == num % i]
    

def prime_factors(num):
    """
    
    :return:
    """
    l = is_prime(num)
    return [1] + l + [num]


def main():
    number = get_number()
    # print(is_prime(number))
    print(prime_factors(number))


if __name__ == '__main__':
    main()
