import random as rand
from boid import Boid
from colors import *

WIDTH, HEIGHT = 1400, 900

class Flock:
    def __init__(self,name="",boids=[],color=RED):
        self.name = name
        self.boids = boids
        self.color = color
    
    def __str__(self):
        ret = f"Flock: {self.name}\n"
        ret += f" - boids: {len(self.boids)}\n"
        ret += f" - color: {self.color}\n"
        return ret
    
    def random_flock(self,size,color):
        self.color = color

        # TODO: why is this needed???
        self.boids = []

        for i in range(size):
            self.add_boid()
    
    def add_boid(self):
        x = rand.randint(0,WIDTH)
        y = rand.randint(0,HEIGHT)
        dir = rand.randint(0,360)
        boid = Boid(x,y,dir,self.color)
        self.boids.append(boid)
    
    def empty(self):
        self.boids = []
    
    def set_color(self,color):
        for boid in self.boids:
            boid.color = color
    
    def clear(self):
        self.boids = []
    