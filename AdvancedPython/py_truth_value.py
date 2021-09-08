from decimal import Decimal


def boolEvaluation(x):
    return bool(x)


if __name__ == '__main__':
    falseValues = [0, [], {}, range(0), 0.0, None, Decimal(0), '', 0j]
    trueValues = [1, [1], {'a': 1}, range(1), 0.01, 'N', Decimal(1)]
    falseResult = map(boolEvaluation, falseValues)
    trueResult = map(boolEvaluation, trueValues)
    print(f'All false values   --> {falseValues} \nTheir bool result --> {list(falseResult)}\n-------------')
    print(f'All true values   --> {trueValues} \nTheir bool result --> {list(trueResult)}')
