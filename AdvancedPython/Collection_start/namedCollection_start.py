import collections

def main():
    Point = collections.namedtuple('Point', 'x y z')
    p1 = Point(5, 9, 0)
    p2 = Point(55, 99, 0)
    print(p1)
    print(p2)
    print(p1.x, p1.y)
    p2 =p2._replace(x=3)
    print(p2)

if __name__ == '__main__':
    main()
