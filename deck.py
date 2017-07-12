from card import Card
import random

class Deck(Card):

    def __init__(self, shuffled=False):
        Card.__init__(self)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.shuffled = shuffled

    def show_deck(self):
        print "The deck is comprised of:", self.deck

    def add_new_card_type(self, suit_type, value_type):
        self.add_new_suit(suit_type)
        self.add_new_value(value_type)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.show_deck()

    def delete_card_type(self, suit_type, value_type):
        self.delete_existing_suit(suit_type)
        self.delete_existing_value(value_type)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.show_deck()

    def create_singular_card_to_deck(self, suit_type, value_type):
        self.create_singular_card(suit_type, value_type)
        self.deck = list(reversed(self.card_list))

    def delete_singular_card_from_deck(self, suit_type, value_type):
        self.delete_singular_card(suit_type, value_type)
        self.deck = list(reversed(self.card_list))

    def shuffle_deck(self):
        random.shuffle(self.deck)
        i=0
        n=0
        while i < (len(self.deck) -1) and n < (len(self.deck) -1):
            if (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) == (self.deck[n], self.deck[n+1]):
                print "Reshuffling..."
                self.shuffle_deck()
            elif (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) != (self.deck[n], self.deck[n+1]) and n < (len(self.deck) -1):
                n+=1
            elif (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) != (self.deck[n], self.deck[n+1]) and n == (len(self.deck) -1):
                i+=1
                n=0
            else:
                return
        else:
            self.shuffled = True
            return self.deck



'''
deck=Deck()
print deck.shuffle_deck()
print deck.show_deck()
print deck.shuffle_deck()
print deck.show_deck()
print deck.shuffled
print deck.add_new_card()
print deck.card_list
'''
