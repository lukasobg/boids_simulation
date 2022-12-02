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
SPEED = 1

def draw_window(universe):
    WIN.fill(BLACK)
    for flock in universe.flocks:
        for boid in flock.boids:
            dir = boid.dir
            dir = dir + rand.randint(-4,4)
            boid.move_in_dir(dir,SPEED)

            # Draw triangle
            tri_boid = boid.get_triangle()
            pygame.draw.polygon(
                surface=WIN, color=boid.color,
                points=tri_boid)

    pygame.display.update()

def main():

    # Boid stuff
    flocks = []
    for i in range(3):
        flock = Flock()
        flock.random_flock(10)
        flocks.append(flock)
    universe = Universe(flocks)

    # Graphical window loop
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window(universe)
    
    pygame.quit()

main()