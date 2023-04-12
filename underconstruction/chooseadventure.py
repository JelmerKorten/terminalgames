#choose your own adventure
#keep on going with this to create bigger

from sys import stdout
from random import uniform
from time import sleep
from os import system

def slow_print(some_string = '', end = '\n', speed_choice = 3, wpm = 50):
    if speed_choice == 6:
        print(some_string)
        return
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
    system('cls || clear')

clear()
print('Before we start: How fast do you want this game to print the text?')

speed_choice = "a"
while not speed_choice.isdigit():
    speed_choice = input('slow (1-5) fast\n>')
    if speed_choice.isdigit():
        speed_choice = int(speed_choice)
        break
    else:
        slow_print("Please provide a number", speed_choice=5)

clear()
slow_print('Do you want to go on an adventure?')
playing = input('(yes/no) ').lower()
if playing == 'no':
    quit()
if playing == 'yes':
    slow_print('Alright, lets go!')
    sleep(1)

clear()
slow_print('What is your name adventurer?')
name = input('')
slow_print(f'Welcome {name}!')
sleep(1)

clear()
slow_print('You are on a road with a T split ahead, which way do you go?')
answer = input('(left/right) ').lower()
if answer == 'right':
    clear()
    slow_print('There is a river ahead, do you walk around or swim through?')
    answer = input('(walk/swim) ').lower()
    if answer == 'swim':
        clear()
        slow_print('you swim through the river')
        slow_print('the water feels cold')
        slow_print('so cold....', wpm=10)
        slow_print('you can not swim anymore and get taken down by the current')
    elif answer == 'walk':
        clear()
        slow_print('you walk around the river')
        slow_print('good choice, it looks cold')
    else:
        clear()
        slow_print('You dont do anything and stand next to the shore.')
        slow_print('.'*6, wpm=10)
        slow_print('a flash flood comes and a tree takes you out..')

elif answer == 'left':
    clear()
    slow_print('You turn left and nearly get hit by a car.')
    slow_print('As you duck away just in time you end up next to the road')
    slow_print(".....", speed_choice=1)
    slow_print("There's a steep hill and you roll down.")
    slow_print("After a long fall you come to rest against a tree.")
    slow_print("Your head is pounding. But you have to keep going..")
    slow_print("When you try to stand up you notice you hurt your ankle.")
    slow_print("This is going to be a l", end="")
    slow_print("oooo",wpm=10,end="")
    slow_print("ng day..")
    sleep(1)
    slow_print("Take some (rest) here or (push) on?")
    user_choice = input("(rest/push)").lower()
    
    if user_choice == "rest":
        clear()
        slow_print("Probably better to sit down here and get some strength back.")
        slow_print("You rest your head against the tree and drift away..")
        slow_print("."*5, wpm=10)
        sleep(1)

else:
    slow_print('Not a valid option.. You keep going straight and smash your head on the wall')
    slow_print('You lose.')

slow_print('Thanks for trying ', end='')
print(f'{name}.')
slow_print('I hope you had fun on this adventure.')
