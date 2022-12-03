import pygame
from colors import *
import random as rand
from universe import Universe
from flock import Flock
from wall import Wall

WIDTH, HEIGHT = 1400, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Boids simulation")

print(pygame.display.list_modes())

FPS = 120
SPEED = 3

# Draw window
def draw_window(universe,noise_off):
    # TODO: dont draw background each time?
    WIN.fill(BLACK)

    # Draw flocks
    for flock in universe.flocks:
        for boid in flock.boids:

            # Draw triangle
            tri_boid = boid.get_triangle(25)
            pygame.draw.polygon(
                surface=WIN, color=boid.color,
                points=tri_boid)

    # Draw walls
    for wall in universe.walls:
        R = pygame.Rect((wall.x, wall.y, wall.size, wall.size))
        pygame.draw.rect(surface=WIN, color=GREY, rect=R, border_radius=4)
        # pygame.draw.circle(WIN, GREY, (wall.x, wall.y), wall.size/2)

    pygame.display.update()

# Main loop
def main():

    # Initialise Universe
    universe = Universe(WIDTH,HEIGHT)
    universe.add_random_flock(1,LIME)
    # universe.add_random_flock(10,RED)
    # universe.add_random_flock(10,BLUE)

    clock = pygame.time.Clock()
    run = True
    pause = True
    noise_off = False

    # Init draw
    draw_window(universe,noise_off)

    # Graphical window loop
    while run:
        clock.tick(FPS)

        # Get events
        for event in pygame.event.get():

            # Quit prgram
            if event.type == pygame.QUIT:
                run = False

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if pause and event.key == pygame.K_RIGHT:
                    draw_window(universe,noise_off)
                if event.key == pygame.K_n:
                    noise_off = not noise_off
                if event.key == pygame.K_c:
                    universe.clear()
                    draw_window(universe,noise_off)
                if event.key == pygame.K_f:
                    universe.add_random_flock(10,rand.choice(COLORS))
                    draw_window(universe,noise_off)

            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    universe.add_wall(pos,25)
                    draw_window(universe,noise_off)

        # Handle multiple/hold events
        keys_pressed = pygame.key.get_pressed()
        if pause and keys_pressed[pygame.K_RIGHT]:
            draw_window(universe,noise_off)
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2]:
            pos = pygame.mouse.get_pos()
            universe.add_wall(pos,25)
            draw_window(universe,noise_off)

        # Update universe
        if not pause:
            universe.update(SPEED) # BOIDS MOVE HERE
            draw_window(universe,noise_off)
    
    pygame.quit()

main()