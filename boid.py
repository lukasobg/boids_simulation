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
    
    def dist_to(self,x,y):
        # TODO: calculate dist across edges
        euc = math.sqrt((self.x-x)**2+(self.y-y)**2)
        return euc

    def dir_to(self,x,y):
        # TODO: calculate dist across edges
        dir_x = x - self.x
        dir_y = y - self.y
        dir = math.atan2(dir_y,dir_x)
        return dir

    def align(self,init_dir,flock):
        RADIUS = 50
        neighbours = 0
        dir = 0
        for n_boid in flock.boids:
            xn,yn = n_boid.x,n_boid.y
            dist_to = self.dist_to(xn,yn)
            if dist_to < RADIUS and dist_to != 0:
                dir += n_boid.dir
                neighbours += 1
            
        if neighbours != 0:
            dir = dir/neighbours
        else:
            dir = init_dir
        
        return dir
    
    def cohesion(self,init_dir,flock):
        RADIUS = 50
        neighbours = 0
        x = 0
        y = 0
        dir = init_dir
        for n_boid in flock.boids:
            xn,yn = n_boid.x,n_boid.y
            dist_to = self.dist_to(xn,yn)
            if dist_to < RADIUS and dist_to != 0:
                x += n_boid.x
                y += n_boid.y
                neighbours += 1
            
        if neighbours != 0:
            x /= neighbours
            y /= neighbours
            self.dir = self.dir_to(x,y)
        
        return dir

    def separate(self,init_dir,flock):
        RADIUS = 50
        neighbours = 0
        dir = 0
        for n_boid in flock.boids:
            xn,yn = n_boid.x,n_boid.y
            dist_to = self.dist_to(xn,yn)
            if dist_to < RADIUS and dist_to != 0:
                dir += n_boid.dir
                neighbours += 1
            
        if neighbours != 0:
            dir = dir/neighbours
        else:
            dir = init_dir

        return dir

    def avoid(self,init_dir,walls):
        RADIUS = 100
        dir = 0
        nowalls = 0
        for wall in walls:
            xw,yw = wall.x, wall.y
            dist_to = self.dist_to(xw,yw)
            if dist_to < RADIUS:
                dir_to = self.dir_to(xw,yw)

                a_force = 1 - dist_to/RADIUS

                # print("START")
                # print(init_dir)
                # print(dir_to)

                a_dir = 0
                if init_dir > dir_to:
                    a_dir = init_dir + a_force*90
                    # print("RIGHT")
                    # print(init_dir)
                    # print(a_dir)
                else:
                    a_dir = init_dir - a_force*90
                    # print("LEFT")
                    # print(init_dir)
                    # print(a_dir)

                dir += a_dir
                nowalls += 1
        
        if nowalls == 0:
            dir =init_dir
        else:
            dir = dir/nowalls
            
        return dir