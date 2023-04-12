#casino script
#which will import games from this folder (hopefully)
#to practice making a slightly bigger project
#and to practice doing custom imports

# from blackjack import blackjack
from roulette import roulette
from blackjack import blackjack
import easygui as eg
import json

# Constants
PATH = 'the-casino/lib/user_chips.json'

# %% load user function (TO BE MOVED TO casino.py)
    # username = ''
def load_user_chips(username):

    try:
        with open(PATH) as f:
            all_user_chips = json.load(f)
    except:
        all_user_chips = {}

    user_chips = all_user_chips.get(username,0)
    
    return user_chips


# %% update user chips in the file
def update_user_chips(username, user_chips):

    try:
        with open(PATH) as f:
            all_user_chips = json.load(f)
    except:
        all_user_chips = {}
    
    #update current user chips
    all_user_chips[username] = user_chips

    with open(PATH, mode='w+') as current_file:
        current_file.write(json.dumps(all_user_chips))



# %% main()
def main():
    menuprint =     '''\t****Welcome to the casino!****
        Available tables:
        [] Blackjack
        [] Roulette
        [] Slotmachines (added soon)
        [] Poker (to be continued)
        [] Quit'''
    
    username = eg.enterbox(msg= "Hello and Welcome to our Casino.\n\nWhat is your username?", title= "Username")
    user_chips = load_user_chips(username)


    while True:
        gameplay = eg.buttonbox(msg = menuprint, title = "Main Menu", choices=["Blackjack", "Roulette", "Slotmachines", "Poker", "Quit"])
        if gameplay == "Quit":
            eg.msgbox(msg = "Have a great day!", title = "Goodbye Message", ok_button="Bye!")
            print(f"User chips after quit msg box, before update call: {user_chips}")
            update_user_chips(username, user_chips)
            print(f"User chips after update_user_chips: {user_chips}")
            quit()
        elif gameplay == "Roulette":
            user_chips = roulette(username, user_chips)
        elif gameplay == "Blackjack":
            user_chips = blackjack(username, user_chips)
            print(f"User chips after blackjack return: {user_chips}")



if __name__ == '__main__':
    main()