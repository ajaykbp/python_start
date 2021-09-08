from collections import Counter

def main():
    fruits1 = ['apple', 'pear', 'banana', 'orange', 'pear', 'banana', 'orange', 'pear']
    fruits2 = ['apple', 'Carrot', 'Beetroot', 'apple', 'pear', 'carrot', 'apple', 'mango']

    counter1 = Counter(fruits1)
    counter2 = Counter(fruits2)
    print(counter1)
    print(counter2)
    print(counter1['pear'])

    print(sum(counter1.values()))

    # counter1.update(fruits2)
    # print(counter1.values())

    print(counter1.most_common(2))
    #counter1.subtract(counter2)
    print(counter1 & counter2)



if __name__ == '__main__':
    main()