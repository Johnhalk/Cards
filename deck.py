from card import Card
import random

class Deck(Card):

    def __init__(self, shuffled=False):
        Card.__init__(self)
        self.deck = self.card_list
        self.shuffle_deck_compare = list(self.card_list)
        self.shuffled = shuffled

    def shuffle_deck(self):
        random.shuffle(self.deck)
        i=0
        while i < (len(self.deck) -1):
            if self.shuffle_deck_compare[i] == self.deck[i]:
                self.shuffle_deck()
                i+=1
            else:
                self.shuffled = True
                return self.card_list


    def add_new_card(self):
        self.add_new_value()
        self.add_new_suit()
        self.deck = self.card_list
        self.shuffle_deck()
        self.show_deck()

    def show_deck(self):
        print "The deck is comprised of: ", self.deck
        print "and is ", len(self.deck) , "cards long"



deck=Deck()
print deck.shuffle_deck()
'''
print deck.show_deck()
print deck.shuffle_deck()
print deck.show_deck()
print deck.shuffled
print deck.add_new_card()
print deck.card_list
'''
