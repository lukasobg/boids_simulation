from flock import Flock
import random as rand
from colors import *

class Universe:
    def __init__(self,width,height,flocks=[]):
        self.width = width
        self.height = height
        self.flocks = flocks

    def add_flock(self,size=10):
        flock = Flock()
        flock.random_flock(size)
        self.flocks.append(flock)
    
    def clear(self):
        for flock in self.flocks:
            flock.clear()
        self.flocks = []
