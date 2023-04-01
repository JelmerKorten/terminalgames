from sys import stdout
from random import uniform
from time import sleep
from os import system, name

def slow_print(some_string = '', end = '\n', speed_choice = 3, wpm = 50):
    random_number = uniform(0.7,1.3)
    for letter in some_string:
        stdout.write(letter)
        stdout.flush()
        sleep((3/speed_choice) * random_number/wpm * 3)
    if end == '\n':
        print('')
    elif end == '':
        print('', end='')

def clear():
    system('cls' if name == 'nt' else 'clear')