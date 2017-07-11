import itertools
import random
from suit import Suit
from value import Value

class Card(Suit, Value):

    def __init__(self):
        Suit.__init__(self)
        Value.__init__(self)
        self.card_list = list(itertools.product(self.suit, self.value))


    def amount_of_cards(self):
        print "The amount of cards are: ", len(self.card_list)

    def add_new_suit(self):
        self.add_suit()
        self.create_card_list()

    def add_new_value(self):
        self.add_value()
        self.create_card_list()

    def delete_exisiting_suit(self):
        self.delete_suit()
        self.create_card_list()
        return self.card_list

    def delete_exisiting_value(self):
        self.delete_value()
        self.create_card_list()
        return self.card_list

    def create_card_list(self):
        self.card_list = list(itertools.product(self.suit, self.value))





'''
card=Card()
print card.value
print card.suit
print card.card_list
print card.amount_of_cards()
card.add_new_suit()
print card.amount_of_cards()
print card.card_list
card.add_new_value()
print card.amount_of_cards()
print card.card_list
card.add_new_value()
print card.amount_of_cards()
print card.card_list
card.add_new_suit()
print card.amount_of_cards()
print card.card_list
print card.delete_exisiting_suit()
print card.delete_exisiting_value()
'''
