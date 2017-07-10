import itertools
import random
from suit import Suit
from value import Value

class Card(Suit, Value):

    def __init__(self):
        Suit.__init__(self)
        Value.__init__(self)
        self.actual_cards = list(itertools.product(self.value, self.suit))


    def amount_of_cards(self):
        print "The amount of cards are: ", len(self.actual_cards)

'''
card=Card()
print card.value
print card.suit
print card.actual_cards
print card.amount_of_cards()
'''
