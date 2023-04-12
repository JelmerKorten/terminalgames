#rock paper scissors game

# TODO:
# - incorporate number of wins
import os
import random
from time import sleep
from math import ceil
clear = lambda: os.system("clear || cls")
user_wins = 0
computer_wins = 0

def print_scoreboard(clr = "n"):
    if clr == "y":
        clear()
    print('|' + '-'*21 + '|')
    print('|----The Score is:----|')
    print('|--  You   VS   PC  --|')
    print(f'|     {user_wins}    -    {computer_wins}     |')
    print('|' + '-'*21 + '|')

options = ['rock', 'paper', 'scissors']
clear()
print('Best of how many games do you want to play?')
best_of = input('(pick an odd number)\n')
if best_of.isdigit():
    best_of = int(best_of)
else:
    print('Please enter a number')

max_wins = ceil(best_of/2)

while user_wins < max_wins and computer_wins < max_wins:
    #print ScoreBoard
    print_scoreboard("y")

    user_input = input('Type: rock/paper/scissors (q to quit)\n').lower()
    if user_input == 'q':
        break
    elif user_input not in options:
        print('Please make a correct option of rock, paper or scissors')
        print('C\'mon, you know how this works..')
        continue
    
    



    computer_pick = random.randint(0,2)
    # 0 = rock | 1 = paper | 2 = scissors
    computer_input = options[computer_pick]
    print(f'Computer picked: {computer_input}.')
    
    if user_input == options[0] and computer_input == options[2]:
        print('You won!')
        user_wins += 1
        # total_wins += 1

    elif user_input == options[1] and computer_input == options[0]:
        print('You won!')
        user_wins += 1
        # total_wins += 1

    elif user_input == options[2] and computer_input == options[1]:
        print('You won!')
        user_wins += 1
        # total_wins += 1
    
    elif user_input == computer_input:
        print('That\'s a tie! Rematch..')
    
    else:
        print('You lost..')
        print('Computer wins!')
        computer_wins += 1
        # total_wins += 1
    sleep(1)

print(f'You won: {user_wins} times')
print(f'Computer won: {computer_wins} times')
print('Final score is:')
print_scoreboard("n")
print('Thank you for playing.\nHave a great day now!')


