from inspect import stack


def isOdd(x):
    return not x % 2 == 0

def checkUpper(x):
    return x.isupper()

def squareOf(x):
    return x ** 2

def main():
    # filter def verify items of sequence through custom methods
    # each item of lst calls by isOdd methods
    lst = [1, 2, 3, 4, 5, 6, 7]
    filteredList = list(filter(isOdd, lst))
    print(filteredList)

    mixedChar = 'nkASjlklKWjjSLerfrFFG'
    upperChar = list(filter(checkUpper, mixedChar))
    print(upperChar)

    sq = list(map(squareOf, lst))
    print(sq)

class A:

    def def_a(self):
        print('inside def_a')
        print('called from -->'+stack()[1].function)


    def def_b(self):
        print('inside def_b')
        print('called from -->'+stack()[1].function)


class B:

    def def_b_a(self):
        a = A()
        print('inside def_b_a')
        print('called from -->'+stack()[1].function)
        a.def_a()

    def def_b_b(self):
        print('inside def_b_b')
        print('called from -->'+stack()[1].function)
        self.def_b_a()


if __name__ == '__main__':
    #main()

    b = B()
    b.def_b_b()