'''
Represents nodes in the problem graph or network.
Locatin coordinates should be passed.
'''

from math import sqrt

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f'({self.getX()},{self.getY()})'
    
    def distanceTo(self, v):
        x_dist = abs(self.getX() - v.getX())
        y_dist = abs(self.getY() - v.getY())
        return sqrt(x_dist * x_dist + y_dist * y_dist)
