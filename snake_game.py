from random import randint
from sys import exit

import pygame
from pygame.locals import *

pygame.init()

width = 650
height = 450
screen = pygame.display.set_mode((width, height))
snake_width = 20
snake_height = 20
food_width = 20
food_height = 20
snake_pos_x = int(width / 2 - snake_width / 2)
snake_pos_y = int(height / 2 - snake_height / 2)
snake_color = 0, 120, 0
snake_size = 10
body_pos = []
padding = food_width
food_pos_x = randint(0 + padding, width - padding)
food_pos_y = randint(0 + padding, height - padding)
food_color = 200, 150, 0
points = 0
clock = pygame.time.Clock()
snake_move_x = 5
snake_move_y = 0
pen = pygame.font.SysFont("Police monospace", 30, True)
eat_sound = pygame.mixer.Sound("./sounds/snake_eat_sound.ogg")
speed = 5
is_dead = False


def draw_snake(body):
    for cordinates in body:
        pygame.draw.rect(
            screen, snake_color, (cordinates[0], cordinates[1], snake_height, snake_width))


def reset():
    global points, snake_pos_x, snake_pos_y, snake_size, body_pos, food_pos_x, food_pos_y, head_pos, is_dead

    points = 0
    snake_pos_x = int(width / 2 - snake_width / 2)
    snake_pos_y = int(height / 2 - snake_height / 2)
    snake_size = 10
    body_pos = []
    food_pos_x = randint(0 + padding, width - padding)
    food_pos_y = randint(0 + padding, height - padding)
    head_pos = []
    is_dead = False


while True:
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Snake game")
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if snake_move_x == speed:
                    pass
                else:
                    snake_move_x = -speed
                    snake_move_y = 0
            if event.key == K_d:
                if snake_move_x == -speed:
                    pass
                else:
                    snake_move_x = speed
                    snake_move_y = 0
            if event.key == K_s:
                if snake_move_y == -speed:
                    pass
                else:
                    snake_move_x = 0
                    snake_move_y = speed
            if event.key == K_w:
                if snake_move_y == speed:
                    pass
                else:
                    snake_move_x = 0
                    snake_move_y = -speed

    snake_pos_x = snake_pos_x + snake_move_x
    snake_pos_y = snake_pos_y + snake_move_y

    snake = pygame.draw.rect(
        screen, snake_color, (snake_pos_x, snake_pos_y, snake_height, snake_width))
    food = pygame.draw.rect(
        screen, food_color, (food_pos_x, food_pos_y, food_height, food_width))
    screen.blit(pen.render(f"score: {points}",
                False, (255, 255, 255)), (500, 40))

    if snake.colliderect(food):
        food_pos_x = randint(padding, width - padding)
        food_pos_y = randint(padding, height - padding)
        points += 1
        eat_sound.play()
        snake_size += 1

    head_pos = []
    head_pos.append(snake_pos_x)
    head_pos.append(snake_pos_y)
    body_pos.append(head_pos)

    if head_pos[0] == width:
        is_dead = True

    if head_pos[0] == 0:
        is_dead = True

    if head_pos[1] == height:
        is_dead = True

    if head_pos[1] == 0:
        is_dead = True

    if len(body_pos) > snake_size:
        del body_pos[0]

    if body_pos.count(head_pos) > 1:
        is_dead = True

    while is_dead:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reset()

        text = pen.render("Você perdeu!", False, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(width / 2, height / 2)))
        pygame.display.update()

    draw_snake(body_pos)

    pygame.display.update()
