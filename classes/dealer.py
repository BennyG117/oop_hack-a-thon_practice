from . import deck
from . import player

class Dealer(player.Player):
    rich = True

    def __init__(self, name='Dealer', hand=[], hand_value = 0, aces = False):
        super().__init__(name, hand, hand_value, aces)
        self.deck = deck.Deck()

    def draw_card(self):
        super().draw_card()

    def play_hand(self):
        # sum = self.hand[0].point_val + self.hand[1].point_val # not correct for now
        super().check_initval(self)

        while self.hand_value < 17:
            # draw_card
            super().draw_card()
            # add new card value to sum
            self.hand_value += self.hand[-1]
            # bust check
            super().ace_bust_check(self, self.hand_value, self.aces)
            # stop if dealer hand is greater than 16
        # else dealer has hand between 17-21
