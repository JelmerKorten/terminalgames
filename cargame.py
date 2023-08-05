import pygame
from pygame.locals import *
from random import randint

pygame.init()
size = WIDTH, HEIGHT = (600,800)
road_width = int(WIDTH/1.6)
road_mark_width = int(WIDTH/80)
right_lane = ((WIDTH/2 + road_width/2 - road_mark_width*3) - WIDTH/2)/2 + WIDTH/2
left_lane = (WIDTH/2 + (WIDTH/2 - road_width/2 + road_mark_width*2.5))/2
CAR_SCALE = 0.5


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racer")


def draw_bg():
    # bg
    screen.fill((60,200,0))
    # road
    pygame.draw.rect(screen, (50,50,50),(WIDTH/2-road_width/2, 0, road_width, HEIGHT))
    # yellow line
    pygame.draw.rect(screen, (255, 240, 60), (WIDTH/2 - road_mark_width/2, 0, road_mark_width, HEIGHT))
    # white line on the right side
    pygame.draw.rect(screen, (235, 235, 235), (WIDTH/2 + road_width/2 - road_mark_width*3, 0, road_mark_width, HEIGHT))
    # white line on the left side
    pygame.draw.rect(screen, (235, 235, 235), (WIDTH/2 - road_width/2 + road_mark_width*2, 0, road_mark_width, HEIGHT))


def load_players():
    # load player
    car = pygame.image.load("src/car2.png")
    car_width = car.get_width()
    car_ratio = (road_width/2 * CAR_SCALE)/car_width
    car = pygame.transform.scale_by(car, car_ratio)
    car_loc = car.get_rect()
    car_loc.center = right_lane ,HEIGHT*0.9

    # enemy
    enemy = pygame.image.load("src/car.png")
    enemy_width = enemy.get_width()
    enemy_ratio = (road_width/2 * CAR_SCALE)/enemy_width
    enemy = pygame.transform.scale_by(enemy, enemy_ratio)
    enemy_loc = enemy.get_rect()
    enemy_len = enemy.get_height()
    print(enemy_len)
    enemy_loc.center = left_lane, HEIGHT*0.1
    return car, car_loc, enemy, enemy_loc, enemy_len

# first screen
draw_bg()
pygame.display.update()
car, car_loc, enemy, enemy_loc, enemy_len = load_players()


# event loop
running = True
speed = 1
dodge_counter = 0
while running:
    enemy_loc[1] += speed
    if enemy_loc[1] > HEIGHT:
        enemy_loc[1] = -enemy_len
        dodge_counter += 1
        if dodge_counter > 4:
            dodge_counter = 0
            speed += 0.25
        if randint(0,1) == 1:
            enemy_loc.centerx = right_lane
        else:
            enemy_loc.centerx = left_lane
            
    # end game
    if enemy_loc[0] == car_loc[0] and enemy_loc[1] > car_loc[1]-enemy_len:
        break
        
    # movement
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc.centerx = left_lane
            if event.key in [K_r, K_RIGHT]:
                car_loc.centerx = right_lane
    
    draw_bg()
    screen.blit(car, car_loc)
    screen.blit(enemy, enemy_loc)
    pygame.display.update()

# quit
pygame.quit()
