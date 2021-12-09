from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
