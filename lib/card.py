import itertools
from lib.suit import Suit
from lib.value import Value

class Card(Suit, Value):

    def __init__(self):
        Suit.__init__(self)
        Value.__init__(self)
        self.card_list = list(itertools.product(self.suit, self.value))

    def create_card_list(self):
        self.card_list = list(itertools.product(self.suit, self.value))

    def amount_of_cards(self):
        print "The amount of cards are:", len(self.card_list)

    def add_new_suit(self, suit_type):
        self.add_suit(suit_type)
        self.create_card_list()

    def add_new_value(self, value_type):
        self.add_value(value_type)
        self.create_card_list()

    def delete_existing_suit(self, suit_type):
        self.delete_suit(suit_type)
        self.create_card_list()
        return self.card_list

    def delete_existing_value(self, value_type):
        self.delete_value(value_type)
        self.create_card_list()
        return self.card_list

    def create_singular_card(self, suit_type, value_type):
        self.card_list.append((suit_type.upper(), value_type.upper()))

    def delete_singular_card(self, suit_type, value_type):
        self.card_list.remove((suit_type.upper(), value_type.upper()))
