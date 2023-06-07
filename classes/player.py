from deck import Deck

class Player:

    def __init__( self, name, hand=[], hand_value=0, aces = False, bust = False):

        self.name = name
        self.hand = hand
        self.hand_value = hand_value
        self.aces = aces
        self.bust = bust
        self.deck = Deck()

#draw a card function(by default when starting draws 2 cards)- add card from hand and remove card from deck
    def draw_card(self):
        self.hand.append(self.deck.cards.pop())
        return self

        

#check value of hand at beginning
    def check_initval(self):
        print('check init is called')
        self.hand_value = 0
        for card in self.hand:
            # checking face cards. Jack - King = 11 - 14, so flatten values to 10
            if card.point_val > 10:
                self.hand_value += 10
            # checking for Aces
            elif card.point_val == 1:
                self.hand_value += 11
                Player.ace_bust_check()
                self.aces = True
            else: # not an Ace or Face card
                self.hand_value += card.point_val
        return self

#when we draw, print out the new hand value
    def show_hand(self):
        self.hand.show_cards()
        return self

# player actions to hit, stay, fold
    def hit_stay(self):
        
        player_action = input('What is your action?')
        # assume player inputs 'hit', 'stay', 'fold'
        if player_action == 'hit':
            # do hit
            self.hand.append(self.deck.cards.pop())
        
        elif player_action == 'stay':
            # do stay
            pass
        elif player_action == 'fold':
            # do fold
            pass
        else: # does not match actions
            print('type hit, stay, or fold')
        return self

#.bust_check(self.hand_value, self.aces)

    def ace_bust_check(self):
        if self.hand_value > 21: # check if hand is greater than 21
            if self.ace_check == True: # check if player has aces
                self.hand_value -= 10 # change Ace value from 11 to 1
                self.ace_check = False
        return self

    

