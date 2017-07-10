class Suit(object):
    
    def __init__(self):
        self.suit = ['H', 'C', 'S', 'D']


    def add_suit(self, suit_type):
        self.suit.append(suit_type)

    def delete_suit(self):
        print "The suits are:", self.suit
        remove_suit = raw_input('Which suit do you want to remove? ')
        if remove_suit in self.suit:
            self.suit.remove(remove_suit)
            return self.suit
        else:
            print "Not a valid suit."



'''
suit_new=Suit()
print suit_new.suit
suit_new.add_suit("T")
print suit_new.suit

suit_new.delete_suit()
print suit_new.suit
'''
