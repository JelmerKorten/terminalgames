# imports
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

    print(f"\nThe first two cards that you've drawn add up to a total of {usernumber}!") # User is shown their first two numbers
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


# TODO:
# - get rid of globals (this code is from long ago)
# - fix initial prints regarding options so user knows what to do.
