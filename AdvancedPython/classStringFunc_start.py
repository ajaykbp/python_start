

class Person():

    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    def __str__(self):
        return f'Person name is {self.name} {self.lname}. He is {self.age} year old'

    def __repr__(self):
        return '<Pesron class - fname:{0} lname:{1} age:{2}>'.format(self.name, self.lname, self.age)

    def __bytes__(self):
        val = f'Person name is {self.name} {self.lname}. He is {self.age} year old'
        val.encode('utf-8')
        return bytes(val.encode('utf-8'))

def main():
    p = Person('Raj', 'Kundra', 45)
    print(p)
    print(repr(p))
    print(bytes(p))

if __name__ == '__main__':
    main()


