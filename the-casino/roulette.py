#roulette game goes here

#https://easygui.readthedocs.io/en/latest/tutorial.html#using-easygui
#https://easygui.sourceforge.net/tutorial.html

# import easygui as eg

# choices = ['Yes', 'No', 'Maybe']

# user_input = eg.enterbox("Input something") #enterbox()
# eg.msgbox("Your input was: " + user_input, title = "This is a msgbox", ok_button = "Button Text") #msgbox(msg, title, button)
# reply = eg.choicebox(msg="What do you want to do?", title="Roulette Menu", choices=choices) #reply = choicebox(msg, choices)


# %% TO DO LIST

# Prio:
# fix payout game logic


# Less prio:
# Add picture for bets
# Add picture + bets overlay
# Add picture + ball lands
# Add picture + overlay bets + ball lands?




def roulette(username, user_chips):

# %% import modules
    import json
    import easygui as eg
    import random



# %% Import User Chips (TO BE MOVED TO casino.py)
    # username = ''
    # def load_user_chips(username):
    #     path = './the-casino/files/user_chips.json'

    #     try:
    #         with open(path) as f:
    #             all_user_chips = json.load(f)
    #     except:
    #         all_user_chips = {}

    #     try:
    #         user_chips = all_user_chips[username]
    #     except:
    #         user_chips = 0
    #     return user_chips


# %% Take Bets
    def take_bets(user_chips):
        user_bets = {}
        bet_choices = ['Red', 'Black', 'Even', 'Odd', '1st 18', '2nd 18', '1st 12', '2nd 12', '3rd 12', '1st column', '2nd column', '3rd column', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        user_choice = eg.buttonbox(f"Do you want to place a bet?", "Your bet:", choices = ["Place a bet", "Let's spin!", "Main Menu"])
        if user_choice == "Main Menu":
            return "", user_chips
        while user_choice != "Let's spin!":
            user_bet_option = eg.choicebox("On what would you like to bet?", "Bet Choice", choices = bet_choices)
            user_bet_amount = eg.integerbox(msg = f"How much would you like to bet on {user_bet_option}?\n\t(0 - {user_chips})", title= "Bet amount", default=0, lowerbound= 0, upperbound= user_chips)
            user_bets.update({user_bet_option: user_bet_amount})
            user_chips -= user_bet_amount
            user_choice = eg.buttonbox(f"You just placed a {user_bet_amount} chips bet on {user_bet_option}", "Your bet:", choices = ["Place (another) bet", "Let's spin!", "Main Menu"])
            if user_choice == "Main Menu":
                return "", user_chips

        eg.msgbox("Spinning the wheel, good luck!", "Spinning")
        
        return user_bets, user_chips


# %% Do something with bets (skipped for now)
    # skip for now


# %% Specify the win conditions for the number the ball is on.
    # aka:
    # it landed on red, even, 1st column, 2nd column etc..
    # specify what colour this number is
    def win_conditions(roulette_spin):

        number_order = [32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        black_numbers = [number for i, number in enumerate(number_order) if i % 2 == 1]
        win_numbers = list(range(1,37))


        colour = ""
        if roulette_spin == 0:
            colour = "Green"
        elif roulette_spin in black_numbers: #the number is black
            colour = "Black"
        else:
            colour = "Red"


        # even or odd:
        even_or_odd = ""
        if roulette_spin == 0:
            pass
        elif roulette_spin % 2 == 0: #the number is even
            even_or_odd = "Even"
        else:
            even_or_odd = "Odd"


        # is the number in 1st 12 - 2nd 12 - 3th 12 of the numbers?
        which_12 = ''
        if roulette_spin == 0:
            pass
        elif roulette_spin in win_numbers[:13]:
            which_12 = 1
        elif roulette_spin in win_numbers[13:25]:
            which_12 = 2
        else:
            which_12 = 3


        # in which half is the number?
        which_18 = ''
        if roulette_spin == 0:
            pass
        elif roulette_spin in win_numbers[:19]:
            which_18 = 1
        else:
            which_18 = 2


        # in which column is the number?
        which_column = ''
        if roulette_spin == 0:
            pass
        elif roulette_spin % 3 == 1: #(1, 4, 7..)
            which_column = 1
        elif roulette_spin % 3 == 2: #(2, 5, 8..)
            which_column = 2
        else: #(spin % 3 == 0, ie: 3, 6, 9..
            which_column = 3

        return colour, even_or_odd, which_12, which_18, which_column



# %% Calculate Payouts

    def calculate_payouts(user_bets, colour, even_or_odd, which_12, which_18, which_column, roulette_spin):

        payout = 0
        for bets, amount in user_bets.items():
            if bets == colour:
                payout += amount * 2
            if bets == even_or_odd:
                payout += amount * 2
            if bets == '1st 18' and which_18 == 1:
                payout += amount * 2
            if bets == '2nd 18' and which_18 == 2:
                payout += amount * 2
            if bets == '1st 12' and which_12 == 1:
                payout += amount * 3
            if bets == '2nd 12' and which_12 == 2:
                payout += amount * 3        
            if bets == '3rd 12' and which_12 == 3:
                payout += amount * 3
            if bets == '1st column' and which_column == 1:
                payout += amount * 3
            if bets == '2nd column' and which_column == 1:
                payout += amount * 3
            if bets == '3rd column' and which_column == 1:
                payout += amount * 3
            if bets == roulette_spin:
                payout += amount * 36
        
        return payout


# %% main function
    def main(username, user_chips):
        while True:
            play_game = eg.buttonbox("Do you want to play a game?", "Play a game?", choices=["Let's Play!", "Main Menu"])
            if play_game == "Main Menu":
                return user_chips
            
            user_bets, user_chips = take_bets(user_chips)
            if user_bets == "":
                return user_chips
            roulette_spin = random.randrange(0,37)
            colour, even_or_odd, which_12, which_18, which_column = win_conditions(roulette_spin)
            eg.msgbox(f"The ball landed on: {colour} {roulette_spin}", "Spin results:")
            payout = calculate_payouts(user_bets, colour, even_or_odd, which_12, which_18, which_column, roulette_spin)
            user_chips += payout
            round_gains = payout - sum(user_bets.values())
            if round_gains <= 0:
                eg.msgbox("No luck this time, play again?", "Checking your bets")
            else:
                eg.msgbox(f"This round you gained a total of {round_gains}, well done!", "Checking your bets")

    user_chips = main(username, user_chips)

    return user_chips

# %% If name main

if __name__ == "__main__":
    roulette("test", 100)