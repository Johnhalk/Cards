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

    def add_new_suit(self, suit):
        if suit not in self.suit:
            self.add_suit(suit)
            self.actual_cards = list(itertools.product(self.value, self.suit))
        else:
            print "Suit already exists"

    def add_new_value(self, value):
        if value not in self.value:
            self.add_value(value)
            self.actual_cards = list(itertools.product(self.value, self.suit))
        else:
            print "Value already exists"

"""
    def add_new_card(self, suit, value):
        if suit not in self.suit and value not in self.value:
            self.add_suit(suit)
            self.add_value(value)
            self.actual_cards = list(itertools.product(self.value, self.suit))
        else:
            print "Can not add that card."
"""




card=Card()
print card.value
print card.suit
print card.actual_cards
print card.amount_of_cards()
card.add_new_suit('Dinosaur')
print card.amount_of_cards()
print card.actual_cards
card.add_new_value('Joker')
print card.amount_of_cards()
print card.actual_cards
card.add_new_value('Ace')
print card.amount_of_cards()
print card.actual_cards
card.add_new_suit('H')
print card.amount_of_cards()
print card.actual_cards
