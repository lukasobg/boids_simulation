import pygame
from boid import Boid
from flock import Flock
import random as rand
from colors import *

WIDTH, HEIGHT = 1400, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Boids simulation")

print(pygame.display.list_modes())

FPS = 120
SPEED = 2.5

def draw_window(flock):
    WIN.fill(BLACK)
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
    clock = pygame.time.Clock()
    run = True
    boid = Boid(450,250,0)
    flock = Flock()
    flock.random_flock(20)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window(flock)
    
    pygame.quit()

main()