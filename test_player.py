import pytest
from player import Player

@pytest.fixture
def player():
    '''Creates new instance of player class'''
    return Player('P1', 'John')

def test_player_initialisation(player):
    assert player.player_id == 'P1'
    assert player.name == 'JOHN'
    assert player.player == ['P1', "JOHN"]
    assert player.hand == []

def test_who_am_i(player, capfd):
    player.who_am_i()
    out, err = capfd.readouterr()
    assert out == "You are P1 JOHN\n"

def test_my_hand(player, capfd):
    player.my_hand()
    out, err = capfd.readouterr()
    assert out == "Your hand is: []\n"
