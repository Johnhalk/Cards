class Suit(object):

    def __init__(self):
        self.suit = ['H', 'C', 'S', 'D']


    def add_suit(self):
        print "The current suits are:", self.suit
        suit_type = raw_input('Which suit do you want to add? ')
        if suit_type.upper() not in self.suit:
            self.suit.append(suit_type.upper())
        else:
            print "Suit already exists."

    def delete_suit(self):
        print "The current suits are:", self.suit
        remove_suit = raw_input('Which suit do you want to remove? ')
        if remove_suit.upper() in self.suit:
            self.suit.remove(remove_suit.upper())
            return self.suit
        else:
            print "Not a valid suit."




'''
suit_new=Suit()
print suit_new.suit
suit_new.add_suit()
print suit_new.suit

suit_new.delete_suit()
print suit_new.suit
'''
