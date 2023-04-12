#choose your own adventure
#keep on going with this to create bigger
from .util import slow_print, clear


print('Before we start: How fast do you want this game to print the text?')
speed_choice = input('(1-5) ')
if speed_choice.isdigit():
    speed_choice = int(speed_choice)
else:
    quit()



slow_print('Do you want to go on an adventure?')
playing = input('(yes/no) ').lower()
if playing == 'no':
    quit()
if playing == 'yes':
    slow_print('Alright, lets go!')

slow_print('What is your name adventurer?')
name = input('')
slow_print(f'Welcome {name}!')

slow_print('You are on a road with a T split ahead, which way do you go?')
answer = input('(left/right) ').lower()
if answer == 'right':
    slow_print('There is a river ahead, do you walk around or swim through?')
    answer = input('(walk/swim) ').lower()
    if answer == 'swim':
        slow_print('you swim through the river')
        slow_print('the water feels cold')
        slow_print('so cold....', wpm=10)
        slow_print('you can not swim anymore and get taken down by the current')
    elif answer == 'walk':
        slow_print('you walk around the river')
        slow_print('good choice, it looks cold')
    else:
        slow_print('You dont do anything and stand next to the shore.')
        slow_print('.'*6, wpm=10)
        slow_print('a flash flood comes and a tree takes you out..')

elif answer == 'left':
    slow_print('picked left')
else:
    slow_print('Not a valid option.. You keep going straight and smash your head on the wall')
    slow_print('You lose.')

slow_print('Thanks for trying ', end='')
print(f'{name}.')
slow_print('I hope you had fun on this adventure.')
