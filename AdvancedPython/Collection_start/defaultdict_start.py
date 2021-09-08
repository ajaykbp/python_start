from collections import defaultdict

def main():
    fruits = ['apple', 'pear', 'banana', 'orange', 'pear', 'banana', 'orange', 'pear']

    fruitCounter = defaultdict(int)
    fruitCounter = defaultdict(lambda : 100)

    for fruit in fruits:
        fruitCounter[fruit] += 1

    #fruitCounter = {}
    # for fruit in fruits:
    #     if fruit in fruitCounter.keys():
    #         fruitCounter[fruit] += 1
    #     else:
    #         fruitCounter[fruit] = 1

    print(fruitCounter)
    for (k, v) in fruitCounter.items():
        print(k, v)

if __name__ == '__main__':
    main()