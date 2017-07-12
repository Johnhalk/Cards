import pytest
from game import Game

@pytest.fixture
def game():
    '''Creates new instance of game class'''
    return Game()

@pytest.fixture
def player(game):
    '''Adds a new player into game class'''
    return game.add_player('john')

@pytest.fixture
def deck_list(game):
    '''contains the list of all cards in a deck upon initialisation.'''
    return game.shuffle_deck_compare

def test_game_initialises(game):
    assert game.deck == deck_list(game)
    assert game.shuffled == False
    assert game.players == []

def test_add_player(game):
    player(game)
    assert game.players[0].name == 'JOHN'
    assert len(game.players) == 1

def test_remove_player(game):
    player(game)
    game.remove_player(1)
    assert game.players == []
    assert len(game.players) == 0

def test_prepare_game(game):
    player(game)
    player(game)
    player(game)
    player(game)
    game.prepare_game()
    assert game.deck != deck_list(game)

def test_prepare_game_two(game):
    game.prepare_game()
    assert game.deck == deck_list(game)

def test_deal_one_card_per_player(game):
    game.deal_one_card_per_player
    assert game.shuffled == False
    assert len(game.deck) == 52

def test_deal_one_card_per_player_two(game):
    player(game)
    player(game)
    player(game)
    player(game)
    game.prepare_game()
    game.deal_one_card_per_player()
    assert len(game.players[0].hand) == 1
    assert len(game.players[1].hand) == 1
    assert len(game.players[2].hand) == 1
    assert len(game.players[3].hand) == 1
    assert len(game.deck) == 48

def test_deal_game(game):
    game.deal_game()
    assert game.shuffled == False
    assert len(game.deck) == 52
    assert len(game.players) == 0

def test_deal_game_two(game):
    player(game)
    player(game)
    player(game)
    player(game)
    game.prepare_game()
    game.deal_game()
    assert game.shuffled == True
    assert len(game.players[0].hand) == 7
    assert len(game.players[1].hand) == 7
    assert len(game.players[2].hand) == 7
    assert len(game.players[3].hand) == 7
    assert len(game.deck) == 24

def test_show_hands(game, capfd):
    player(game)
    game.show_hands()
    out, err = capfd.readouterr()
    assert out == "There are currently 1  Players in the game.\nJOHN currently has []\n"

def test_show_hands_two(game, capfd):
    player(game)
    game.deal_one_card_per_player()
    game.show_hands()
    out, err = capfd.readouterr()
    assert out == "There are currently 1  Players in the game.\nJOHN currently has [('H', 'ACE')]\n"

def test_start_game(game):
    game.start_game()
    assert game.shuffled == False
    assert len(game.deck) == 52

def test_start_game_two(game):
    player(game)
    player(game)
    player(game)
    player(game)
    game.start_game()
    assert game.shuffled == True
    assert len(game.players[0].hand) == 7
    assert len(game.players[1].hand) == 7
    assert len(game.players[2].hand) == 7
    assert len(game.players[3].hand) == 7
    assert len(game.deck) == 24
