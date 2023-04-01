# string = 'helloodfssb'

# string1 = string[:len(string)]
# print(string)
# print(string1)

print("### Welcome to the Casino! ###")

usernumber = 0


import random
from time import sleep

randomhitorstand = ["hit", "stand"]

rngnumber = random.randint(2000, 10000)
startingmoney = 10000
botchoice = random.choice(randomhitorstand)


def blackjack():
    global usernumber
    global startingmoney
    usernumber = 0
    botnumber = 0

    try:
        while True:
            bet = int(input("\nPlace your bet: "))
            if bet <= 1999 and startingmoney > 2000:
                print("That amount is too low to be considered a real bet!")
            elif bet > startingmoney:
                print(f"You do not have enough money brokey! You currently only have {startingmoney}")
            else:
                print(f"You will be playing against a bot who has placed a bet of {rngnumber} dollars!")
                break
    except:
        print("Invalid Input. Please try again.")

    hitnumber = random.randint(1, 10)
    usernumber += hitnumber
    hitnumber = random.randint(1, 10)
    usernumber += hitnumber
    # Here the user receives their first two cards

    hitnumber = random.randint(1, 10)
    botnumber += hitnumber
    # Here the dealer gets their first card ONLY so that it can be revealed to the user.

    startingnumbers = print(f"\nThe first two cards that you've drawn add up to a total of {usernumber}!") # User is shown their first two numbers
    sleep(2)
    print(f"The dealers first card is {botnumber}") # dealers first card is revealed
    sleep(2)
    print("\nQuick tip, the dealer must always hit while being under the number 17 but always must stand if the number is equal to or greater than 17.")
    while usernumber < 21: # While the users number is below 21, it would always ask the user if they would like to hit or stand.
        hitorstand = input(f"\nWould you like to hit or stand?: ")
        if hitorstand == "hit" or hitorstand[0].lower() == "h":
            hitnumber = random.randint(1, 10) # hitnumber is randomised from 1-10
            usernumber += hitnumber # if they decide to hit then they would have "hitnumber" added to their own number
            print(f"You have decided to hit! You now have a sum total of {usernumber}!")
        if usernumber > 21:
            startingmoney -= bet # if the user reaches a number above 21 then they would lose the bet automatically and lose the amount they bet
            print(f"Unfortunately you've reached a number over 21, Game over. You now only have {startingmoney} left to play with :(")
            return
        if usernumber == 21: # If they land a perfect 21 then they automatically win
            startingmoney += bet # money added to their credit
            print(f"Congratulations, you've scored a perfect 21 and have managed to double the money you bet! You now have {startingmoney} :)")
        if hitorstand == "stand" or hitorstand[0].lower() == "s": # now if the user decides to stand, the dealer would start to play.
            print(f"You've decided to stand on your current number ({usernumber}), the dealer will now play.")
            break

    hitnumber = random.randint(1, 10)
    botnumber += hitnumber
    # dealer receives his 2nd card
    print(f"\nThe dealers first two cards add up to a total of {botnumber}!")
    while botnumber < 17: # While the dealer has a number below 17, they will be forced to hit.
        hitnumber = random.randint(1, 10)
        botnumber += hitnumber
        sleep(2)
        print(f"The dealer has hit and now has a total of {botnumber}!")

        if  botnumber < 17:
            hitnumber = random.randint(1,10)
            botnumber += hitnumber
            sleep(2)
            print(f"The dealer has hit once again and now has a total of {botnumber}!")

        if botnumber > 21: # if the dealer goes over the number 21 then the user wins
            startingmoney += bet
            sleep(2)
            print(f"The dealer has busted by going over 21 and you're now considered the winner! You now have {startingmoney}")
            return
        break

    while botnumber >= 17:
        sleep(2)
        print(f"The dealer now stands on the number {botnumber} and the winner will be decided shortly")
        # Here it would go through multiple situations regarding the dealers and users number
        if botnumber > usernumber: # if dealernumber is higher than the usersnumber then the user has lost and loses the amount he bet
            startingmoney -= bet
            sleep(1)
            print(f"Unfortunately, the bot has managed to earn themselves a number above yours.")
            sleep(2)
            print(f"\nYou've lost the bet and you now only have {startingmoney} dollars left to play with :(")
        elif botnumber < usernumber: # if the user number is higher than the dealers number then he would receive 2x the money he bet
            startingmoney += bet
            sleep(2)
            print(f"Fortunately, you've managed to earn yourself a number higher than the bot! You now have {startingmoney}")
        elif botnumber == usernumber: # if the user number is equal to the dealers number then the user would get their money back
            startingmoney += bet
            sleep(1)
            print(f"Somehow the both of you have managed to end up with the same number.")
            sleep(2)
            print(f"This will be considered a draw and you've gotten your money back.")
        break

rngNumber2 = random.randint(1, 10)

def guessthenumber():
    global startingmoney
    attempts = 3
    try:
        while True:
            bet2 = int(input("\nWhat is the amount that you would like to bet?: "))
            if bet2 <999:
                sleep(1)
                print("Brokey, bet some more money.")
            elif bet2 > startingmoney:
                sleep(1)
                print(f"Brokey, you do not have enough money to bet that much! You only have {startingmoney}")
            else:
                sleep(1)
                print("\nLet's get started.")
                break
    except:
        sleep(1)
        print("Invalid input. Please try again.")

    sleep(1)
    print("A random number between 1 and 10 has been generated and now you will be given 3 attempts to guess the correct number!")
    sleep(1)
    guess = int(input(f"Guess the number (You have {attempts} attempts left): "))
    while guess != rngNumber2:
        attempts -= 1
        guess = int(input(f"\nIncorrect! Try again. Guess the number (You have {attempts} attempts left): "))
        if attempts == 0:
            startingmoney -= bet2   
            print(f"Unlucky you, you've run out of attempts which means you've lost! You now only have {startingmoney} left to play with.")
            return
            startingmoney -= bet2
            print(f"Unfortunately, you've run out of attempts because you suck! You now only have {startingmoney} left to play with.")
        if guess == rngNumber2:
            print(f"You have guessed correctly! You have now earned yourself a whopping {bet2}")

def slotmachine():
    print("this is a scam machine")


print('''Select which game you would like to play
    1. Blackjack
    2. Guess The Number
    3. Jackpot Slot Machine
    4. blah blah blah
    5. blah blah blah
    6. Leave Casino''')

while True:
    selection = input("\nSelect the game (6 to leave): ")

    if selection == "1" or selection[0].lower() == "b":
        blackjack()
    elif selection == "2" or selection[0].lower() == "g":
        guessthenumber()
    elif selection == "6" or selection[0].lower() == "l":
        quit()