# 找零问题
"""

https://github.com/taizilongxu/interview_python#12-%E6%89%BE%E9%9B%B6%E9%97%AE%E9%A2%98

https://www.cnblogs.com/xsyfl/p/6938642.html
"""


def coinChange(values, valuesCounts, money, coinsUsed):
    """
    贪心算法：局限，取决于values的值，可能有的就不能求出解。
        如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
        表面上这道题可以用贪心算法，但贪心算法无法保证可以求出解，比如1元换成2元的时候
    
    https://www.cnblogs.com/xsyfl/p/6938642.html
    
    :param values: 硬币的面值
    :param valuesCounts: 钱币对应的种类数
    :param money: 找出来的总钱数
    :param coinsUsed: 对应于目前钱币总数i所使用的硬币数目
    :return:
    """
    # 遍历出从1到money所有的钱数可能
    for cents in range(1, money + 1):
        #
        minCoins = cents
        # 把所有的硬币面值遍历出来和钱数做对比，尽可能找出最大的零钱
        for kind in range(0, valuesCounts):
            if (values[kind] <= cents):
                temp = coinsUsed[cents - values[kind]] + 1
                if (temp < minCoins):
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print('面值:{0}的最少硬币使用数为:{1}'.format(cents, coinsUsed[cents]))


def coin_change(money, values, collection):
    """
    贪心算法递归获取尽可能大的面值
    :param money:
    :param values:
    :param collection:
    :return:
    """
    temp = money
    if [v for v in values if v <= temp]:
        for kind in values:
            if kind <= temp:
                collection.append(kind)
                temp -= kind
        if temp > 0:
            return coin_change(temp, values, collection)

    return temp


def coin_change_complete(money, values, collection):
    # TODO 判断是否存在完全解

    return


if __name__ == '__main__':
    values = [50, 20, 10, 5, 1]
    money = 78
    coinsUsed = [0] * (money + 1)
    # coinChange(values, len(values), money, coinsUsed)
    
    result = []
    print(coin_change(money, values, result), result)
    

