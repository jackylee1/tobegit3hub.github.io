+++
date = "2016-01-10T08:35:30+08:00"
draft = true
title = "snake game in python"

+++



## Requirement

* pygame

## Code

<pre><code>
import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 20 # the number of squares
WINDOW_HEIGHT = 20 # the number of squares
UNIT = 20 # the pixel of each square

pygame.init()
time_clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH*UNIT,WINDOW_HEIGHT*UNIT),0,32)
pygame.display.set_caption('snake')

snake = []
for i in range(0,5):
    snake.insert(0,[i,0]) # the snake is (2,0) (1,0) (0,0)
food = [10,10] # the food is (10,10)
move_left = False
move_right = True
move_up = False
move_down = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and move_right==False:
                move_left = True
                move_right = False
                move_up = False
                move_down = False
            if event.key == K_RIGHT and move_left==False:
                move_left = False
                move_right = True
                move_up = False
                move_down = False
            if event.key == K_UP and move_down==False:
                move_left = False
                move_right = False
                move_up = True
                move_down = False
            if event.key == K_DOWN and move_up==False:
                move_left = False
                move_right = False
                move_up = False
                move_down = True

    for i in range(len(snake)-1): # most node move to it's the previous node's position
        index = len(snake) - i - 1 # copy the snake from back to front
        snake[index][0] = snake[index-1][0]
        snake[index][1] = snake[index-1][1]
        
    # move the head, 0 for x and 1 for y 
    if move_left == True:
        snake[0][0] -= 1
    if move_right == True:
        snake[0][0] += 1
    if move_up == True:
        snake[0][1] -= 1
    if move_down == True:
        snake[0][1] += 1
   
    # todo(kiic): implement the logic to eat food and hit the wall
    ''' 
    if head.right<0 or head.left>WINDOWWIDTH or head.bottom<0 or head.top>WINDOWHEIGHT:
        break
    if food.left == snakeRect[0].left-1 and food.top == snakeRect[0].top-1:
        food.left = random.randint(0,WINDOWWIDTH/20-1)*(rectLength+2)
        food.top = random.randint(0,WINDOWHEIGHT/20-1)*(rectLength+2)
    else:
         snakeRect.pop(len(snakeRect)-1)
    '''

    window.fill((255, 255, 255)) # draw the background
    for i in range(len(snake)):
        snake_node_rect = pygame.Rect(snake[i][0]*UNIT, snake[i][1]*UNIT, UNIT, UNIT)
        pygame.draw.rect(window,(255, 0, 0), snake_node_rect) # draw the snake
    food_rect = pygame.Rect(food[0]*UNIT, food[1]*UNIT, UNIT, UNIT)
    pygame.draw.rect(window,(0, 255, 0),food_rect) # draw the food

    pygame.display.update()
    time_clock.tick(10)    
</code></pre>
