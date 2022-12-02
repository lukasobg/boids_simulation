import math
from colors import *

WIDTH, HEIGHT = 1400, 900

def highlight(str):
    print()
    print("----------------------------")
    print(str)
    print("----------------------------")
    print()

class Boid:

    def __init__(self, x, y, dir, color=RED):
        self.x = x
        self.y = y
        self.dir = dir
        self.color = color
    
    def get_triangle(self,height=20):

        dir_rad = math.radians(self.dir)
        x = self.x + height * math.cos(dir_rad)
        y = self.y + height * math.sin(dir_rad)
        points = [(x,y)]
        for diff in [math.radians(90),-math.radians(90)]:
            xs = self.x + 1/4*height * math.cos(dir_rad+diff)
            ys = self.y + 1/4*height * math.sin(dir_rad+diff)
            points.append((xs,ys))
    
        return points

    def set_xy(self,x,y):
        self.x = x
        self.y = y

    def set_dir(self,dir):
        self.dir = dir
    
    def move_in_dir(self,dir,speed):
        self.dir = dir
        x = self.x + speed * math.cos(math.radians(dir)) 
        y = self.y + speed * math.sin(math.radians(dir)) 

        if x > WIDTH: x = 0
        if x < 0: x = WIDTH
        if y > HEIGHT: y = 0
        if y < 0: y = HEIGHT

        self.x = x
        self.y = y
