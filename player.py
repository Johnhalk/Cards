class Player(object):

    def __init__(self, name):
        self.name = name.upper()
        self.hand = []

    def who_am_i(self):
        print "You are" , self.name

    def my_hand(self):
        print "Your hand is:", self.hand

"""player1=Player('P1','John')
print player1.who_am_i()
print player1.player


player2=Player('P2','Eammon')
print player2.who_am_i()
print player2.player

print player2.hand
print player1.hand"""
