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
SPEED = 3

def draw_window(universe):
    WIN.fill(BLACK)
    for flock in universe.flocks:
        for boid in flock.boids:
            # Move boid in random direction
            dir = boid.dir
            dir = dir + rand.randint(-4,4)
            boid.move_in_dir(dir,SPEED)

            # Align boid
            boid.align(flock)

            # Cohese boid
            boid.cohesion(flock)

            # Draw triangle
            tri_boid = boid.get_triangle()
            pygame.draw.polygon(
                surface=WIN, color=boid.color,
                points=tri_boid)

    pygame.display.update()

def main():

    # Boid stuff
    universe = Universe(WIDTH,HEIGHT)
    for i in range(1):
        universe.add_flock(10)

    # Graphical window loop
    clock = pygame.time.Clock()
    run = True
    pause = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if pause and event.key == pygame.K_RIGHT:
                    draw_window(universe)

        # Handle multiple keys pressed same time
        # keys_pressed = pygame.key.get_pressed()
        # if pause and keys_pressed[pygame.K_RIGHT]:
        #     draw_window(universe)

        if not pause:
            draw_window(universe)
    
    pygame.quit()

main()