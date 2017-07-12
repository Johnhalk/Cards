from deck import Deck
from player import Player
import random

MAX_START_OF_HAND = 7
MIN_NUMBER_OF_PLAYERS_REQUIRED = 4

class Game(Deck, Player):

    def __init__(self):
        Deck.__init__(self, shuffled=False)
        self.players = []

    def add_player(self, name):
        new_player = Player(name.upper())
        self.players.append(new_player)
        print "There are currently", len(self.players) , " Players in the game."

    def remove_player(self, player):
         del self.players[player - 1]

    def prepare_game(self):
        if len(self.players) < MIN_NUMBER_OF_PLAYERS_REQUIRED:
            return "Not enough players to start game."
        else:
            self.shuffle_deck()
            print self.shuffled
            print self.deck

    def deal_one_card_per_player(self):
            i=0
            while i < len(self.players):
                draw_card = self.deck.pop()
                self.players[i].hand.append(draw_card)
                i += 1

    def deal_game(self):
        if len(self.players) < MIN_NUMBER_OF_PLAYERS_REQUIRED:
            return "Not enough players to start game."
        n=0
        while n < MAX_START_OF_HAND  and len(self.players[len(self.players)-1].hand) < MAX_START_OF_HAND :
            self.deal_one_card_per_player()
            n+=1

    def show_hands(self):
        i=0
        while i < len(self.players):
            print self.players[i].name, "currently has" , self.players[i].hand
            i += 1

    def start_game(self):
        self.prepare_game()
        self.deal_game()


"""game=Game()
game.deck
game.add_player('P1', 'John')
game.add_player('P2', 'Eammon')
game.add_player('P3', 'Jane')
game.add_player('P4', 'Anthony')
print game.players

print game.prepare_game()
print game.deal_one_card_per_player()
print game.deal_one_card_per_player()

print game.players[0].hand
print game.players[1].hand
print game.players[2].hand


print game.deck
print len(game.deck)"""
