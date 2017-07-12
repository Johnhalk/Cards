import pytest
from player import Player

@pytest.fixture
def player():
    '''Creates new instance of player class'''
    return Player('John')

def test_player_initialisation(player):
    assert player.name == 'JOHN'
    assert player.hand == []

def test_who_am_i(player, capfd):
    player.who_am_i()
    out, err = capfd.readouterr()
    assert out == "You are JOHN\n"

def test_my_hand(player, capfd):
    player.my_hand()
    out, err = capfd.readouterr()
    assert out == "Your hand is: []\n"
