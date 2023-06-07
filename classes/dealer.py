from deck import Deck
from player import Player

class Dealer(Player):

    def __init__(self, name='Dealer', hand=[], hand_value = 0, aces = False, bust = False):
        super().__init__(name, hand, hand_value, aces, bust)
        self.deck = Deck()
    
    def draw_card(self):
        super().draw_card()
        return self

    def play_hand(self):
        super().check_initval()
        print(self.hand_value)
        while self.hand_value < 17:
            print('went into while loop')
            # draw_card
            super().draw_card()
            # add new card value to sum
            print(self.hand[-1].point_val)
            self.hand_value += self.hand[-1].point_val
            # check if bust whle holding an ace
            super().ace_bust_check()
        # else dealer has hand between 17-21
        # show dealer hand
        super().show_hand()
        # check if dealer busted
        if self.hand_value > 21:
            self.bust = True
        return self


dealer = Dealer()
dealer.draw_card().draw_card().play_hand()





# dealer.hand[0].card_info()
# dealer.hand[1].card_info()



