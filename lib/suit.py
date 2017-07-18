class Suit(object):

    def __init__(self):
        self.suit = ['H', 'C', 'S', 'D']


    def add_suit(self, suit_type):
        if suit_type.upper() not in self.suit:
            self.suit.append(suit_type.upper())
        else:
            print "Suit already exists."

    def delete_suit(self, suit_type):
        if suit_type.upper() in self.suit:
            self.suit.remove(suit_type.upper())
            return self.suit
        else:
            print "Not a valid suit."
