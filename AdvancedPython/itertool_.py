import itertools

def main():
    lst = ['Sun', 'Mon', 'Tue']

    # itertool.cycle as name suggest its keeps cycling sequence value
    res = itertools.cycle(lst)
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))

    # simple counter with step
    cnt = itertools.count(100)
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))

    # accumulate keeps adding previous values, in case of string keeps appending strings
    lst = [54, 80, 11, 22, 33, 44, 55, 66]
    res = itertools.accumulate(lst)
    res2 = itertools.accumulate(lst, max) # additional function we can pass
    print(list(res))
    print(list(res2))

    # use chain to connect sequences together
    lst = ['ABCD','12345']
    res = itertools.chain('ABCD','12345','yhakd')
    print(list(res))

    def functTrue(x):
        return x <= 40

    def functFalse(x):
        return True

    lst = [10, 20, 30, 40, 50, 60, 70, 80]
    # dropwhile and takewhile will return the value untill a certain condition met that stop them
    # dropwhile works untill prdicateFunction return true and takewhile untill function value false
    print(list(itertools.dropwhile(functTrue, lst))) # drop the value untill that condition match, pick after that
    print(list(itertools.takewhile(functTrue, lst))) # take value until that condition match, leave after that
    print(list(itertools.product(lst,repeat=2)))

if __name__ == '__main__':
    main()