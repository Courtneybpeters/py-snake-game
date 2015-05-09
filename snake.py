# TODO: Squares are not moving on an equal grid so they can move very easily
#       and get off aligned so to make it impossible to collide.


import pygame, sys, random, util
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake")
screen_rect = screen.get_rect()
screen_center = screen_rect.center

fps_clock = pygame.time.Clock()

# Colors
green = pygame.Color(55, 186, 35)
black = pygame.Color(0, 0, 0)
purple = pygame.Color(83, 15, 119)

# Font
font = pygame.font.Font('Fishfingers.ttf', 40)
lose_msg = font.render("Game Over.", True, black)
score = 0


# Shapes
body_rect = Rect(50, 50, 30, 30)

f_width = random.randrange(0, 641)
f_top = random.randrange(0 , 481)
food_rect = Rect(f_width, f_top, 30, 30)

# Speed of snake
slow = .5
faster = 1
fastest = 1.5

# Inital Direction
side = 'left'
direction = 1

while True:

    screen.fill(green)

    score_msg = font.render((str(score)), False, black)
    screen.blit(score_msg, (0, 0))

    pygame.draw.rect(screen, black, body_rect)
    pygame.draw.rect(screen, purple, food_rect)

    util.move(body_rect, fastest, side, direction)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            starting = False
            if event.key == K_DOWN:
                side = 'top'
                direction = 1
            elif event.key == K_UP:
                side = 'top'
                direction = 0
            elif event.key == K_LEFT:
                side = 'left'
                direction = 0
            elif event.key == K_RIGHT:
                side = 'left'
                direction = 1

    # TODO: Squares are not lining up
    if body_rect.contains(food_rect):
        score += 1

    # TODO: This should detect with it hits, not if it's out of it.
    if not screen_rect.contains(body_rect):
        screen.blit(lose_msg, (180, 180))

    pygame.display.update()
    fps_clock.tick(30)
