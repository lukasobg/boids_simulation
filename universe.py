from flock import Flock
from wall import Wall
from colors import *
import math
import random as rand

class Universe:
    def __init__(self,width,height,flocks=[],walls=[]):
        self.width = width
        self.height = height
        self.flocks = flocks
        self.walls = walls

    def add_random_flock(self,size,color):
        flock = Flock()
        flock.random_flock(size,color)
        self.flocks.append(flock)
    
    def mousepos_to_wall_pos(self,mousepos,size):
        x = mousepos[0]
        y = mousepos[1]
        x-=10
        y-=10

        margin = 6
        gui_size = int(size + 2*margin)
        mid_point = int(gui_size/2)
        no_walls_x = self.width / gui_size
        no_walls_y = self.height / gui_size

        no_walls_x -= 2
        no_walls_y -= 2

        x_anchors = [xa for xa in range(mid_point,self.width-mid_point,gui_size)]
        y_anchors = [ya for ya in range(mid_point,self.height-mid_point,gui_size)]

        min_x = math.inf
        x_ = 0
        for xa in x_anchors:
            if abs(x-xa) < min_x:
                min_x = abs(x-xa)
                x_ = xa

        min_y = math.inf
        y_ = 0
        for ya in y_anchors:
            if abs(y-ya) < min_y:
                min_y = abs(y-ya)
                y_ = ya

        return x_,y_

    def add_wall(self,mousepos, size):
        x,y = self.mousepos_to_wall_pos(mousepos,size)
        wall = Wall(x,y,size)
        self.walls.append(wall)
    
    def clear(self):
        for flock in self.flocks:
            flock.clear()
        self.flocks = []
    
    def update(self,SPEED):

        # Draw flocks
        for flock in self.flocks:

            for boid in flock.boids:

                dir = boid.dir

                # Random dir
                rdir = dir + rand.randint(-4,4)

                # Align boid
                adir = boid.align(dir,flock)

                # Cohese boid
                cdir = boid.cohesion(dir,flock)

                # Separate boid
                sdir = boid.separate(dir,flock)

                # Avoid walls
                odir = rdir
                if self.walls:
                    odir = boid.avoid(dir,self.walls)

                # Total direction
                rand_weight = 25
                a_weight = 1
                c_weight = 1
                s_weight = 1
                o_weigt = 10
                sum_weigths = rand_weight+a_weight+c_weight+s_weight+o_weigt

                tot_dir = rand_weight*rdir+a_weight*adir+c_weight*cdir+s_weight*sdir+o_weigt*odir
                tot_dir /= sum_weigths
                tot_dir %= 360

                # TODO: better way to deal with noise (only draw?)
                # if noise_off:
                #     tot_dir = (tot_dir+dir)/2

                # Move boid
                boid.move_in_dir(tot_dir,SPEED)
