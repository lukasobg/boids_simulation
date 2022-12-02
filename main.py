import pygame
from boid import Boid
import random as rand

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Boids simulation")

print(pygame.display.list_modes())

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

FPS = 120
SPEED = 4

def draw_window(boid):
    WIN.fill(BLACK)

    # Draw triangle
    tri_boid = boid.get_triangle(40)
    pygame.draw.polygon(
        surface=WIN, color=RED,
        points=tri_boid)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    boid = Boid(450,250,0)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window(boid)
        x = boid.x
        if x > WIDTH:
            x = 0
        y = boid.y
        dir = boid.dir
        dir = dir + rand.randint(-4,4)
        # boid.set_xy(x+1,y)
        boid.move_in_dir(dir,SPEED)
    
    pygame.quit()

main()