# Find Cost of Tile to Cover W x H Floor
"""
Calculate the total cost of tile it would take to cover a floor plan
of width and height, using a cost entered by the user.

计算瓦片的总成本，以覆盖楼层平面图
宽度和高度，使用用户输入的成本。

referer:
https://github.com/Drhealsgood/miniprojects/blob/master/number_projects/other/misc.py

** https://stackoverflow.com/questions/46018433/nameerror-name-cost-is-not-defined-when-calling-function
"""

costToCover = lambda w, h, ppm: w * h * ppm


def find_max_comb(seq):
    temp = 0
    for i, n in enumerate(seq):
        for v in seq[i + 1:]:
            temp = max(temp, n + v)
    return temp


def main1():
    """ Find max combination of 2 numbers in a sequence - n^2 """
    cost, width, height = map(int, input("Enter 3 space separated integers: ").split())
    print(costToCover(width, height, cost))
    print(find_max_comb([1, 7, 3, 1, 3, 5, 4]))


def cost_o_tile():
    while True:
        cost = int(input("Cost of each tile:"))
        width = int(input("What is the width of the floor?"))
        height = int(input("What is the height of the floor?"))
        try:
            if cost < 0 or width < 0 or height < 0:
                print("\n Please enter non-negative integers")
                break
            else:
                return ("In order to cover your {} X {} floor, you will need to pay {} dollars".format(
                    width, height, cost * width * height))
        except ValueError:
            print("No valid integer! Please try again ...")


def main():
    print("NOTE: The unit of cost is in dollars and dimension unit is in feet")
    cost_o_tile()


if __name__ == '__main__':
    main1()

