from . import deck
from . import player

class Dealer(player.Player):

    def __init__(self, name='Dealer', hand=[], hand_value = 0, aces = False, bust = False):
        super().__init__(name, hand, hand_value, aces, bust)
        self.deck = deck.Deck()
        return self
    
    def draw_card(self):
        super().draw_card()
        return self

    def play_hand(self):
        # sum = self.hand[0].point_val + self.hand[1].point_val # not correct for now
        super().check_initval(self)
    
        while self.hand_value < 17:
            # draw_card
            super().draw_card()
            # add new card value to sum
            self.hand_value += self.hand[-1]
            # check if bust whle holding an ace
            super().ace_bust_check(self, self.hand_value, self.aces)
        # else dealer has hand between 17-21
        # show dealer hand
        super().show_hand(self)
        # check if dealer busted
        if self.hand_value > 21:
            self.bust = True
        return self
