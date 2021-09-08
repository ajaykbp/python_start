from math import pi  # import goes on top


#   2blank lines between classes and outer methods
class Calc:

    def printPi(self):
        print(pi)

    # 1blank line between inner methods
    def usepi(self):
        result = 2 * pi
        print(result)


if __name__ == '__main__':
    cObj = Calc()
    cObj.printPi()
    cObj.usepi()
