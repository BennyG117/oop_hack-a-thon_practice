from classes.deck import Deck
from classes.player import Player
from classes.dealer import Dealer
import random #add random built-in

# bicycle = Deck()

# random.shuffle(bicycle.cards) #shuffle deck

# bicycle.show_cards() #shows shuffled deck

# for reference
# player_cards = []
# player_cards.append(bicycle.cards.pop()) 

#get a card from the deck - will show as an array


#(while loop) while sum of players hand is <= 21, game will continue to run 

# when you break over 21 break condition (you lose!) // start over 

# ...eventually dealer bust option too


# blackjack Order of Operations
# auto - Dealer deals cards to dealer and player
# Dealers cards are hidden
# Player actions (hit, stay, fold)
# auotmatic - Dealer (hit, stay) - dealer keeps hittig if hand value < 17
# automatic - compare hands, determine winner

# all pseudo-code, not working code below
# parent - Player
# child - Player, Dealer

gambler1 = Player('John')

dealer = Dealer('Aaron')

# dealer.bust_check()

# checked during game

# dealer.hand_value >= gambler1.hand_value

# if player == 21 && dealer == 21, draw

print(gambler1.draw_card())

# print(dealer.)