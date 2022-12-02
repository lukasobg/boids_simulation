import random as rand
from boid import Boid

WIDTH, HEIGHT = 1400, 900

class Flock:
    def __init__(self,boids=[]):
        self.boids = boids
    
    def random_flock(self,size):
        for i in range(size):
            self.add_boid()
    
    def add_boid(self):
        x = rand.randint(0,WIDTH)
        y = rand.randint(0,HEIGHT)
        dir = rand.randint(0,360)
        boid = Boid(x,y,dir)
        self.boids.append(boid)
    
    def empty(self):
        self.boids = []
    
    def set_color(self,color):
        for boid in self.boids:
            boid.color = color