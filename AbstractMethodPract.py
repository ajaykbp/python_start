from abc import ABC, abstractmethod


class GraphicShapes(ABC):
    #def __init__(self):
        #super.__init__()

    @abstractmethod
    def calcArea():
        pass


class Circle():

    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShapes):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


c = Circle(2)
print(c)
s = Square(6)
res = s.calcArea()
print(res)
