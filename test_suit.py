from suit import Suit
import pytest

@pytest.fixture
def suit():
    '''Creates new instance of suit class.'''
    return Suit()

def test_suit_initialisation(suit):
    assert suit.suit == ['H', 'C', 'S', 'D']

def test_add_suit(suit):
    suit.add_suit('T')
    assert suit.suit == ['H', 'C', 'S', 'D', 'T']

def test_add_suit_two(suit, capfd):
    suit.add_suit('H')
    out, err = capfd.readouterr()
    assert out == "Suit already exists.\n"

def test_delete_suit(suit):
    suit.delete_suit('H')
    assert suit.suit == ['C', 'S', 'D']

def test_delete_suit_two(suit, capfd):
    suit.delete_suit('Joker')
    out, err = capfd.readouterr()
    assert out == "Not a valid suit.\n"
