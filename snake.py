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
font = pygame.font.SysFont('helvetica', 32)
lose_msg = "Game Over."
score = 0


# Shapes
body_rect = Rect(50, 50, 15, 15)

f_width = random.randrange(0, 641)
f_top = random.randrange(0 , 481)
food_rect = Rect(f_width, f_top, 15, 15)

# Speed of snake
slow = 1
faster = 2
fastest = 3

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

    if body_rect.colliderect(food_rect):
        score += 1

    pygame.display.update()
    fps_clock.tick(30)
