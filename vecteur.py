from math import sqrt

class Vector:

    #initialization
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #magic method to customize object representation
    def __repr__(self):
        # here you can what you should do if you want to create the object
        # use this when you want to write something for another developer that will use your code
        return f'Vector1{self.x}, {self.y}'

    # magic method to customize what is returned by the print function
    def __str__(self):
        # this is like a print method
        return f'This is to print that Vector1=({self.x}, {self.y})'

    def norm(self):
        n = sqrt(self.x**2+self.y**2)
        return n
    def sum(self, t):
        self.x+=t.x
        self.y+=t.y

    def sub(self, t):
        self.x-=t.x
        self.y-=t.y

v1 = Vector(x=3, y=0)
v2 = Vector(x=6, y=3)

v1.sum(v2)
v1.sub(v2)
