class MyClolor():

    def __init__(self, red, green):
        self.red = red
        self.green = green

    def __repr__(self):
        return '<MyColor red:{0} green:{1}>'.format(self.red, self.green)

    def __add__(self, other):
        return MyClolor(self.red + other.red, self.green + other.green)

    def __sub__(self, other):
        return MyClolor(self.red - other.red, self.green - other.green)

    def __eq__(self, other):
        return MyClolor(self.red == other.red, self.green == other.green)

    def __gt__(self, other):
        return MyClolor(self.red > other.red, self.green > other.green)

def main():
    p1 = MyClolor(40, 50)
    p2 = MyClolor(20, 30)

    print(p1)
    print(p1+p2)
    print(p1-p2)
    p3 = MyClolor(20,30)
    print(p2 == p3)
    print(p2 > p3)

if __name__ == '__main__':
    main()