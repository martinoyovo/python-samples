from math import sqrt

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norme(self):
        n = sqrt(self.x**2+self.y**2)
        return n
    def sum(self, t):
        self.x+=t.x
        self.y+=t.y

v1 = Vecteur(x=3, y=0)
v2 = Vecteur(x=6, y=3)

v1.sum(v2)
