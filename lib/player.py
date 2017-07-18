class Player(object):

    def __init__(self, name):
        self.name = name.upper()
        self.hand = []

    def who_am_i(self):
        print "You are" , self.name

    def my_hand(self):
        print "Your hand is:", self.hand
