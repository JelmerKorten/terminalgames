# using turtle to create a camel race that can be bet on.
# no controls to "help" the camel yet.

import turtle as t
import time
from random import shuffle, randint

WIDTH, HEIGHT = 600, 600
COLOURS = ['red','blue','cyan','yellow','orange','pink','black','green','teal','navy']


def get_colours(racers):
    shuffle(COLOURS)
    colours = COLOURS[:racers]
    
    return colours

def create_camels(colours, spacing):
    camels = []
    camel_speed = 3
    if len(colours)>5:
        camel_speed = 5
    for idx in range(len(colours)):
        camel = t.Turtle()
        camel.speed(camel_speed)
        camel.color(colours[idx])
        camel.shape('turtle')
        camel.left(90)
        camel.penup()
        camel.goto((-WIDTH//2) + spacing*(idx+1),-HEIGHT//2+20)
        camel.pendown()
        camels.append(camel)
    
    return camels

def calc_spacing(racers):
    return WIDTH // (racers + 1)

def init_screen():
    screen = t.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racer")
    liner = t.Turtle()
    liner.speed(8)
    liner.penup()
    liner.goto(-WIDTH//2,-HEIGHT//2+20)
    liner.pendown()
    liner.goto(WIDTH//2,-HEIGHT//2+20)
    liner.penup()
    liner.color("red")
    liner.goto(-WIDTH//2,HEIGHT//2-20)
    liner.pendown()
    liner.goto(WIDTH//2,HEIGHT//2-20)

    while True:
        racers = screen.numinput("Number of Racers","How many racers are racing today?",3,2,10)
        if racers:
            racers = int(racers)
            break
    
    return racers, screen

def race():
    racers, screen = init_screen()
    spacing = calc_spacing(racers)
    colours = get_colours(racers)
    camels = create_camels(colours,spacing)
    
    while True:
        for camel in camels:
            dist = randint(2,15)
            camel.forward(dist)
            _, y = camel.pos()
            if y >= HEIGHT // 2 -32:
                return camel.pencolor()
 

winner = race()
print(f"The winner of the race is the {winner.title()} Turtle!!")
time.sleep(2)

