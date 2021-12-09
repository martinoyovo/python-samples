from math import sqrt

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norme(self):
        n = sqrt(self.x**2+self.y**2)
        return n


v = Vecteur(x=3, y=9)
print(v.norme())