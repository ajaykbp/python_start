from collections import OrderedDict

def main():
    d = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
    print(d)
    r=OrderedDict(d)
    print(r)


if __name__ == '__main__':
    main()