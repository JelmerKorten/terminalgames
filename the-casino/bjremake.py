# Recreating blackjack using classes
from random import choices

class Card:
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face
        
    def __repr__(self):
        return f"{self.face}of{self.suit}"

class Stack:
    def __init__(self, decks=4):
        self.faces = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.suits = ['Diamonds','Hearts','Clubs','Spades']
        self.cards = self.create_stack(decks)
        self.population = list(self.cards.keys())
        self.weights = list(self.cards.values())
        
    def create_stack(self, decks = 4):
        card_deck = []
        for suit in self.suits:
            for face in self.faces:
                card_deck.append(Card(suit,face))
        return {card: decks for card in card_deck}
    
    def get_card(self):
        # get random card + it's count in stack
        card = choices(self.population, self.weights)
        card_count = self.cards.get(card)
        # update stack and weights for realistic odds
        self.cards.update({card:card_count -1})
        self.weights = list(self.cards.values())
        # return the chosen card
        return card

class Hand:
    def __init__(self, holder):
        self.owner = holder
        self.score = 0
        self.Aces = []
        self.cards = []
    
    def __repr__(self):
        return f"{self.cards} worth {self.score}"
    
    def reset(self):
        self.cards = []
        
    def add(self,card):
        self.cards.append(card)
        if card.face == "Ace":
            self.Aces.append(True)

    def calc(self):
        # for every card in the hand
        for card in self.cards:
            # if it's K,Q,J, 
            if card.face in ['King', 'Queen', 'Jack']:
                if self.score + 10 > 21 and len(self.Aces) > 0:
                    self.Aces.pop(0)
                else:
                    self.score += 10
            elif card.face == "Ace":
                # self.Aces.append(True)
                if self.score + 11 > 21 and len(self.Aces) > 0:
                    self.score += 1
                    self.Aces.pop(0)
                else:
                    self.score += 11
            else:
                if self.score + card.face > 21 and len(self.Aces) > 0:
                    self.score = self.score - 10 + card.face
                    self.Aces.pop(0)
                else:
                    self.score += card.face
                    
        return self.score
    
    def display(self):
        self.score = self.calc()
        print(self)
        
        


class BlackJack:
    def __init__(self, player_name, coins):
        self.stack = Stack()
        self.name = player_name
        self.house_name = "house"
        self.player_hand = Hand(self.name)
        self.house_hand = Hand(self.house_name)
        self.coins = coins

    def first_deal(self):
        self.player_hand.add(self.stack.get_card())
        self.house_hand.add(self.stack.get_card())
        self.player_hand.add(self.stack.get_card())
        
    def show_state(self):
        # print player hand
        self.player_hand.display()
        # print house hand
        self.house_hand.display()



# # %% blackjack() for import
# def blackjack(username, user_chips):

#     # %% import modules
#     from random import choices
#     import easygui as eg
#     # import json (only needed to load chips)

#     #we gonna use a dict
#     #make a card deck

#     # %% create card stack function
#     def create_stack():
#         cards = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
#         houses = ['ofDiamonds','ofHearts','ofClubs','ofSpades']
#     #card_deck = dict(zip(houses, numbers))

#     #combine numbers and houses
#         card_deck = []
#         for house in houses:
#             for card in cards:
#                 card_deck.append(str(card) + ' ' + house)

#     #using 4 decks to make a stack to give user a bit better chance
#         card_stack = {k: 4 for k in card_deck}
#         return card_stack


#     # %% setup game function
#     #set up a game with x players
#     def setup_game(card_stack, username, number_of_players = 1):
#         #create a list with player names (for now player1 through playern)
#         number_of_players = int(number_of_players)
#         if number_of_players == 1:
#             players = [username]
#         else:
#             players = []
#             for i in range(1, number_of_players+1):
#                 players.append("player" + str(i))
        
#         #create player hands dict
#         playerhands = {}

#         #set initial population
#         #population stays the same, weights just get to zero so they won't get picked
#         population = list(card_stack.keys())
        
#         #dealing first cards
#         for player in players:
            
#             #update weights every round to keep odds correct with real life
#             weights = list(card_stack.values())
            
#             #update the player's cards
#             playerhands.update({player: choices(population,weights)})
            
#             #get the old amount of the chosen card
#             old_value = card_stack.get(playerhands.get(player)[-1])
            
#             #update the card_stack so we can calculate new weights
#             card_stack.update({playerhands.get(player)[-1] : old_value - 1})


#         ##house first card
#         househand = {}
#         weights = list(card_stack.values())
#         househand.update({'house': choices(population,weights)})
#         old_value = card_stack.get(househand.get('house')[0])
#         card_stack.update({househand.get('house')[0] : old_value - 1})

#         return card_stack, playerhands, househand



#     # %% calculate hand score function
#     def calculate_score(hand):
#         score = 0
#         Aces = []
#         for card in hand:
#             card_value = card.split()[0]
#             if card_value in ['King', 'Queen', 'Jack']:
#                 if score + 10 > 21 and len(Aces) > 0:
#                     Aces.pop(0)
#                 else:
#                     score += 10

#             elif card_value == "Ace":
#                 Aces.append(True)
#                 if score + 11 > 21 and len(Aces) > 0:
#                     score += 1
#                     Aces.pop(0)
#                 else:
#                     score += 11

#             else:
#                 card_value = int(card_value)
#                 if score + card_value > 21 and len(Aces) > 0:
#                     score = score - 10 + card_value
#                     Aces.pop(0)
#                 else:
#                     score += card_value
        
#         return score


#     # %% the game logic
#     def the_game(playerhands, card_stack, househand):
#         population = list(card_stack.keys())
#         #do this for every player
#         playerscores = []
#         for player in playerhands:

#             #every player gets a 2nd card before they get an option
#             weights = list(card_stack.values())
#             current_hand = playerhands.get(player)
#             new_card = choices(population,weights)[0]
#             current_hand.append(new_card)
#             playerhands.update({player: current_hand})
#             old_value = card_stack.get(new_card)
#             card_stack.update({new_card : old_value - 1})
#             score = calculate_score(playerhands.get(player))



#             while score < 21:
#                 score = calculate_score(playerhands.get(player))
#                 selection = eg.buttonbox(msg= f"""Currently playing: {player}
#                 You now have the following hand:
#                 {playerhands.get(player)}
#                 This adds up to a total of: {score}
#                 The house has a {househand.get("house")}
                
#                 Do you want to hit or stand?""", title= "What do you do?", choices= ["Hit", "Stand"])
#                 # print(f'currently playing: {player}')  
#                 # print(f'You now have the card(s) {playerhands.get(player)}')
#                 # print(f'Adding up to a total of: {score}')
#                 # print(f'The house has a {househand.get("house")}')
            
#                 # selection = input('Do you want to hit or stand?\n').lower()
#                 if selection == "Hit":
#                     weights = list(card_stack.values())
#                     current_hand = playerhands.get(player)
#                     new_card = choices(population,weights)[0]
#                     current_hand.append(new_card)
#                     playerhands.update({player: current_hand})
#                     old_value = card_stack.get(new_card)
#                     card_stack.update({new_card : old_value - 1})

#                 elif selection == "Stand":
#                     break
#                 else:
#                     print('Please provide a valid option.')

#                 #to check for while loop condition    
#                 score = calculate_score(playerhands.get(player))
            
#             #to print statement after you have busted so you know what you have.
#             eg.msgbox(msg= f"""You ended with the the hand:
#             {playerhands.get(player)}
#             This is worth {score}, your turn is over""", title= "Turn is over")
#             # print(f'You ended with the card(s) {playerhands.get(player)}')
#             # print(f'Adding up to a total of: {score}, your turn is over.')
#             playerscores.append(score)

#         #players have now finished
#         # check if there are still players who havent busted
        
#         valid_playerhands = {k:v for k,v in playerhands.items() if calculate_score(v) <= 21}
#         if len(valid_playerhands) == 0:
#             return playerhands, card_stack, househand

#         for player in playerhands:
#             if len(playerhands.get(player)) == 2 and calculate_score(playerhands.get(player)) == 21 and calculate_score(househand.get('house')) < 10:
#                 #player has a blackjack, the house is not able to get 21.
#                 eg.msgbox(msg= "Looks like you have a blackjack and the house does not", title= "Blackjack")



#         #Dealer will now play
#         dealer_score = calculate_score(househand.get('house'))
#         while dealer_score < 17:
#             weights = list(card_stack.values())
#             current_hand = househand.get('house')
#             new_card = choices(population,weights)[0]
#             current_hand.append(new_card)
#             househand.update({'house': current_hand})
#             old_value = card_stack.get(new_card)
#             card_stack.update({new_card : old_value - 1})

#             eg.msgbox(f"""The house gets another card and has:
#             {househand.get("house")}""")
#             # print(f'The house gets another card and has: {househand.get("house")}')

#             dealer_score = calculate_score(househand.get('house'))

#         return valid_playerhands, card_stack, househand


#     # %% combining it all in main()
#     def main(username, user_chips):
        
#         number_of_players = eg.buttonbox(msg= """Hello, welcome to the blackjack table
#         With how many players do you want to play?""", title= "Number of players?", choices= ["1", "2"])
#         # username = input('What is your username?\n')
#         # username = "player1"
#         # number_of_players = int(input('With how many players do you want to play?\n'))

        
#         #create new stack
#         card_stack = create_stack()
#         full_stack_count = sum(card_stack.values())

#         #load_user_chips
#         # user_chips = load_user_chips(username)
#         # user_chips = 100 # comment out above and use this for sharing + testing

#         eg.msgbox(msg = f"Welcome to the Blackjack Table, {username}, we have loaded your chips.", title= "Welcome", ok_button="Thank you!")
#         # print(f'Welcome {username}, we have loaded your chips.')
        
#         # %% ## BELOW TO BE MOVED TO casino.py
#         # selection = input('Would you like to add more?\n')

#         # if selection.lower() in ['yes', 'y']:
#         #     add_chips = input('How much do you want to add?\n')
#         #     if add_chips.isdigit():
#         #         user_chips += int(add_chips)
#         ##potentially add while loop to make sure we get right inputs here
#         # print(f"Alright! You now have {user_chips} at your disposal, have fun in the casino!")
#         # print('May the odds be ever in your favour.')
#         ## ABOVE TO BE ADDED TO casino.py
#         # %% cont

#         while True:
#             place_bet = eg.buttonbox(msg= f"\t\tYou have {user_chips} chips", title= "Player", choices=["Let's play!", "Main Menu"])
#             # print(f'You have {user_chips} chips,\nplace a bet to start the game (or q to quit)')
#             # place_bet = input('')
#             if place_bet == "Main Menu":
#                 eg.msgbox("Thanks for playing Blackjack\nHave a great day!", ok_button= "Cya!")
#                 # print('Have a good day.')
#                 return user_chips
#             else:
#                 place_bet = eg.integerbox(msg= "How much do you want to bet?", title= "Bets", default= 10, lowerbound= 1,upperbound=None)
#                 if user_chips < place_bet:
#                     eg.msgbox(msg= "You do not have this amount of chips.")
#                     # print('You do not have this amount of chips.')
#                 else:
#                     user_chips -= place_bet
#                     card_stack, playerhands, househand = setup_game(card_stack, username, number_of_players)

#                     # update_user_chips(username, user_chips) # comment out for sharing

#                     playerhands, card_stack, househand = the_game(playerhands, card_stack, househand)

#                     #calculate winner and bet payouts
#                     for player in list(playerhands.keys()):
#                         player_score = calculate_score(playerhands.get(player))
#                         house_score = calculate_score(househand.get('house'))

#                     #player and house not busted and player wins
#                     if player_score < 22 and house_score < 22 and player_score > house_score:
#                         user_chips += place_bet*2
#                         eg.msgbox(f"""\t\t\tThe house has {house_score} while you have {player_score}
#                         This means you win!
#                         You gained {place_bet*2} and now have {user_chips} chips!""",
#                         ok_button= "Sweet!")                        
#                         # print(f'The house has {house_score} while you have {player_score}')
#                         # print('This means you win!')
#                         # print(f'You gained {place_bet*2} and now have {user_chips} chips')
                    
#                     #player and house not busted and house wins
#                     elif player_score < 22 and house_score < 22 and player_score < house_score:
#                         eg.msgbox(f"""\t\t\tThe house has {house_score} while you have {player_score}
#                         This means you lose
#                         You lost your {place_bet} chips bet and now have {user_chips} chips""")
#                         # print(f'The house has {house_score} while you have {player_score}')
#                         # print('This means you lose')
#                         # print(f'You lost your {place_bet} chips bet and now have {user_chips} chips')

#                     #player and house not busted and tie
#                     elif player_score < 22 and house_score < 22 and player_score == house_score:
#                         eg.msgbox(f"It's a tie! You both have {player_score} and you will get back your bet", ok_button= "So close..")
#                         # print(f'It\'s a tie! You both have {player_score} and you will get back your bet')
#                         user_chips += place_bet
                    
#                     #player alive and house busted
#                     elif player_score < 22 and house_score >= 22:
#                         user_chips += place_bet*2
#                         eg.msgbox(f"""\t\t\tThe house has busted and you have {player_score}
#                         You win, gain {place_bet*2} chips and now have {user_chips} chips.""", ok_button= "Nice!")
#                         # print(f'The house has busted and you have {player_score}')
#                         # print(f'You win, gain {place_bet*2} chips and now have {user_chips} chips')
                    
#                     #player busted
#                     elif player_score >= 22:
#                         eg.msgbox(msg= "You busted and you lose your bet.", ok_button= "Yikes")
#                         # print('You busted and you lose your bet')
                    
#                     #player has blackjack, house does not
#                     elif len(playerhands.get(player)) == 2 and player_score == 21 and len(househand.get("house")) > 2:
#                         eg.msgbox(msg= "You have a blackjack and the house does not!\nYou gain 3x your bet.", title= "Blackjack!")
#                         user_chips += place_bet * 3
#                     else:
#                         eg.msgbox(msg= "I'm not sure what happened, code debug needed!")
#                         # print('Im not sure what happened, code Debug needed!')
                    

#                     #check remaining card_stack size and reshuffle if less than 40% remaining.
#                     if sum(card_stack.values()) < full_stack_count*0.4:
#                         card_stack = create_stack()
#                         eg.msgbox(msg= """\t\tReshuffling the cards, this will only take a second!
#                         *****************************
#                         Card have been shuffled and the dealer is ready for another round!""",
#                         ok_button= "Let's go!")
#                         # print('Reshuffling the cards, this will only take a second')
#                         # print('********************')
#                         # print('Cards have been shuffled and the dealer is ready for another round!')

#     user_chips = main(username, user_chips)

#     return user_chips

# if __name__ == "__main__":
#     blackjack(username="test", user_chips=100)
