def main():
    lst = [100, 101, 102, 103, 104, 105]
    # any and all to test sequence of bool value
    print(any(lst))
    print(all(lst))

    # min, max and sum builtin methods
    print(min(lst))
    print(max(lst))
    print(sum(lst))

    # -------------Iterator methods-----------#
    # Iter
    iteratedList = iter(lst)
    print(next(iteratedList))
    print(next(iteratedList))
    print(f'after using 2 times next method {list(iteratedList)}')

    with open('./resources/test.txt', 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line)

    for x in range(len(lst)):
        print(f'{x} {lst[x]}')

    # enumerate returns collection value along with index
    for x, i in enumerate(lst, 1):
        print(f'{x} {i}')

    # zip maps two sequence
    lst1 = [1, 2, 3, 4, 5]
    lst2 = ['a', 'b', 'c', 'd', 'e']
    z = zip(lst1, lst2)
    print(dict(z))

if __name__ == '__main__':
    main()
