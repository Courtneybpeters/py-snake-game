# TODO: Squares are not moving on an equal grid so they can move very easily
#       and get off aligned so to make it impossible to collide.


import pygame, sys, random
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
white = pygame.Color(255, 255, 255)
purple = pygame.Color(83, 15, 119)

# Font
font = pygame.font.Font('Fishfingers.ttf', 40)
title_font = pygame.font.Font('Fishfingers.ttf', 80)
lose_msg = font.render("Game Over.", True, black)
new_msg = font.render("New Game", True, white)
title = title_font.render('Py-Snake', True, black)
score = 0

# Speed of snake
slow = 4
faster = 10
fastest = 20

# Testing purposes
CHOSEN_SPEED = faster

# Generate food
def new_food():
    food_left = random.randrange(0, 641 - 40, 40)
    food_top = random.randrange(0 , 481 - 40, 40)
    food_rect = Rect(food_left, food_top, 40, 40)
    return food_rect

# Shapes
body_rect = Rect(50, 50, 40, 40)
food = new_food()

# Buttons
new_game = Rect(200, 200, 150, 50)
new_game.left = screen_center[0] - 50
new_game.top = screen_center[1] + 50
#
#start_game = Rect(200, 200, 150, 50)
#start_game.center = screen_center

# Move function
def move(rect, speed, direction):
    rect.left += speed * direction[0]
    rect.top += speed * direction[1]

# Inital location and direction
location = body_rect.left, body_rect.top
direction = (1,0)
started = False

# State
state = 'start menu'


while True:
    
    if state == 'in game':

        screen.fill(green)
    
        score_msg = font.render((str(score)), False, black)
        screen.blit(score_msg, (0, 0))
    
        pygame.draw.rect(screen, black, body_rect)
        pygame.draw.rect(screen, purple, food)
    
        move(body_rect, CHOSEN_SPEED, direction)
        
        # Food collision check
        if body_rect.contains(food):
            score += 1
            food = new_food()
        
        # Wall collision check
        if not screen_rect.contains(body_rect):
            state = 'game over'
      
    if state == 'game over':
        screen.fill(green)
        screen.blit(lose_msg, (200, 200))
        pygame.draw.rect(screen, black, new_game) 
        screen.blit(new_msg, (new_game.left + 10, new_game.top + 10))
        
    if state == 'start menu':
        screen.fill(green)
        screen.blit(title, (screen_center[0] - 10, screen_center[1] - 10))
        pygame.draw.rect(screen, black, new_game) 
        screen.blit(new_msg, (new_game.left + 10, new_game.top + 10))     

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            
            if new_game.collidepoint(click):
                state = 'in game'

        elif event.type == KEYDOWN:
            started = False
            if event.key == K_DOWN:
                direction = (0,1)
            elif event.key == K_UP:
                direction = (0,-1)
            elif event.key == K_LEFT:
                direction = (-1,0)
            elif event.key == K_RIGHT:
                direction = (1,0)          

    pygame.display.update()
    fps_clock.tick(CHOSEN_SPEED)
