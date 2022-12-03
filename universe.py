from flock import Flock
from colors import *

class Universe:
    def __init__(self,width,height,flocks=[]):
        self.width = width
        self.height = height
        self.flocks = flocks

    def add_random_flock(self,size,color):
        flock = Flock()
        flock.random_flock(size,color)
        self.flocks.append(flock)
    
    def clear(self):
        for flock in self.flocks:
            flock.clear()
        self.flocks = []
