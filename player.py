class Player(object):

    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.player = [player_id, name]
        self.hand = []

    def who_am_i(self):
        print "Hello,", self.name, "You are" , self.player_id



"""player1=Player('P1','John')
print player1.who_am_i()
print player1.player


player2=Player('P2','Eammon')
print player2.who_am_i()
print player2.player

print player2.hand
print player1.hand"""
