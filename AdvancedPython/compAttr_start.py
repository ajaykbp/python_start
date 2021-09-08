class MyClolor():

    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use gettattr to to dynamically return a value
    def __getattr__(self, item):
        if item == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif item == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            return AttributeError

    # use gettattr to to dynamically return a value
    def __setattr__(self, key, value):
        if key == 'rgbcolor':
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(key, value)

    # use dir to list the available properties
    def __dir__(self):
        return ['red', 'green', 'blue', 'rgbcolor']

def main():
    p = MyClolor()

    # print the value of computed attr
    print(p.rgbcolor)
    print(p.hexcolor)

    # set the value of computed attr
    p2 = MyClolor()
    p2.rgbcolor = (125, 200, 86)
    print(p2.rgbcolor)
    print(p2.hexcolor)

    # list all attr of class
    print(dir(p2))


if __name__ == '__main__':
    main()
