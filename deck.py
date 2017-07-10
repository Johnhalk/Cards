from card import Card
import random

class Deck(Card):

    def __init__(self):
        Card.__init__(self)
        self.deck = self.actual_cards


    def show_deck(self):
        print "The deck is comprised of: ", self.actual_cards
        print "and is ", len(self.actual_cards) , "cards long"


    def shuffle_deck(self):
        deck_list = self.actual_cards
        random.shuffle(deck_list)
        return deck_list



deck=Deck()
print deck.show_deck()
print deck.shuffle_deck()
print deck.show_deck()
