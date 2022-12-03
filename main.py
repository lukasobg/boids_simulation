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

def draw_window(universe,noise_off):
    # TODO: dont draw background each time?
    WIN.fill(BLACK)

    # Draw flocks
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

            # Avoid walls
            odir = rdir
            if universe.walls:
                odir = boid.avoid(dir,universe.walls)

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

def main():

    # Boid stuff
    universe = Universe(WIDTH,HEIGHT)
    universe.add_random_flock(1,LIME)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    universe.add_wall(pos,25)
                    draw_window(universe,noise_off)

        # Handle multiple keys pressed same time
        keys_pressed = pygame.key.get_pressed()
        if pause and keys_pressed[pygame.K_RIGHT]:
            draw_window(universe,noise_off)
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2]:
            pos = pygame.mouse.get_pos()
            universe.add_wall(pos,25)
            draw_window(universe,noise_off)

        if not pause:
            draw_window(universe,noise_off)
    
    pygame.quit()

main()