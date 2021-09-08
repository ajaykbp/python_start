from dataclasses import dataclass


@dataclass
class Book:
    bookName: str
    author: str
    price: int


if __name__ == '__main__':
    b = Book('3 point someone', 'Chetan Bhagat', 250)
    b2 = Book('3 point someone', 'Chetan Bhagat', '')
    #print(b)
    print(b == b2)
