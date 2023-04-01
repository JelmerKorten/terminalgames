#a number guess game
import random

print('How big of a range do you want to guess in...?')
top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a positive number..\nyou know, the ones larger than zero')
        quit()
else:
    print('Please type a number next time..')
    quit()



random_number = random.randint(0,top_of_range) #11 included
# r = random.randrange(-5,11) #11 not included
print(random_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input('Take a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time..')
        continue

    if random_number == user_guess:
        print('That\'s it, you found the number!')
        break
    elif random_number > user_guess:
        print('A bit higher...')
    else:
        print('Noo, not that high!')

print(f'You found the right number in {guesses} guesses!\nThat\'s impressive!')
