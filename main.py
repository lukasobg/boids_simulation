import pygame
from universe import Universe
from flock import Flock
import random as rand
from colors import *

WIDTH, HEIGHT = 1400, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Boids simulation")

print(pygame.display.list_modes())

FPS = 120
SPEED = 2

def draw_window(universe,noise_off):
    WIN.fill(BLACK)
    for flock in universe.flocks:
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

            # Total direction
            rand_weight = 3
            a_weight = 1
            c_weight = 1
            s_weight = 1
            sum_weigths = rand_weight+a_weight+c_weight+s_weight

            tot_dir = rand_weight*rdir+a_weight*adir+c_weight*cdir+s_weight*sdir
            tot_dir /= sum_weigths

            # TODO: better way to deal with noise (only draw?)
            if noise_off:
                tot_dir = (tot_dir+dir)/2

            # Move boid
            boid.move_in_dir(tot_dir,SPEED)

            # Draw triangle
            tri_boid = boid.get_triangle(40)
            pygame.draw.polygon(
                surface=WIN, color=boid.color,
                points=tri_boid)

    pygame.display.update()

def main():

    # Boid stuff
    universe = Universe(WIDTH,HEIGHT)
    universe.add_random_flock(8,GREEN)
    # universe.add_random_flock(10,RED)
    # universe.add_random_flock(10,BLUE)

    # Graphical window loop
    clock = pygame.time.Clock()
    run = True
    pause = True
    noise_off = False
    draw_window(universe,noise_off)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if pause and event.key == pygame.K_RIGHT:
                    draw_window(universe,noise_off)
                if event.key == pygame.K_n:
                    noise_off = not noise_off

        # Handle multiple keys pressed same time
        keys_pressed = pygame.key.get_pressed()
        if pause and keys_pressed[pygame.K_RIGHT]:
            draw_window(universe,noise_off)

        if not pause:
            draw_window(universe,noise_off)
    
    pygame.quit()

main()