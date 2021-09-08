
class Book(object):
    def __init__(self, bookname, author, price):
        self.bookname = bookname
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book Name {self.bookname}, Book Author {self.author}"

    def __repr__(self):
        return f"repr Book Name {self.bookname}, Book Author {self.author}"

    def __ge__(self, value):
        if not isinstance(value, Book):
            return ValueError('Can not compare Book with Non Book object')
        return self.price >= value.price

    def __eq__(self, value):
        if not isinstance(value, Book):
            return ValueError('Can not compare Book with Non Book object')
        return (self.bookname == value.bookname and
                self.author == value.author)

def main():
    print('running main')
    b = Book('Wings of fire', 'A P J Abdul Kalaam', 120)
    b2 = Book('Wings of fire', 'A P J Abdul Kalaam1', 120)
    print(b == b2)
    print(b >= b2)
    # print(b)
    print(repr(b))
