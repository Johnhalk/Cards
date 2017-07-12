import pytest
from deck import Deck

@pytest.fixture
def deck():
    '''Creates new instance of deck class.'''
    return Deck()

@pytest.fixture
def card_list(deck):
    '''contains the list of all cards upon initialisation.'''
    return deck.card_list

def test_deck_initialisation(deck):
    assert deck.card_list == card_list(deck)
    assert deck.deck ==  list(reversed(card_list(deck)))
    assert deck.shuffled == False

def test_add_new_card(deck):
    deck.add_new_card('T','Joker')
    assert deck.deck == [('T', 'JOKER'), ('T', 'KING'), ('T', 'QUEEN'), ('T', 'JACK'), ('T', '10'), ('T', '9'), ('T', '8'), ('T', '7'), ('T', '6'), ('T', '5'), ('T', '4'), ('T', '3'), ('T', '2'), ('T', 'ACE'), ('D', 'JOKER'), ('D', 'KING'), ('D', 'QUEEN'), ('D', 'JACK'), ('D', '10'), ('D', '9'), ('D', '8'), ('D', '7'), ('D', '6'), ('D', '5'), ('D', '4'), ('D', '3'), ('D', '2'), ('D', 'ACE'), ('S', 'JOKER'), ('S', 'KING'), ('S', 'QUEEN'), ('S', 'JACK'), ('S', '10'), ('S', '9'), ('S', '8'), ('S', '7'), ('S', '6'), ('S', '5'), ('S', '4'), ('S', '3'), ('S', '2'), ('S', 'ACE'), ('C', 'JOKER'), ('C', 'KING'), ('C', 'QUEEN'), ('C', 'JACK'), ('C', '10'), ('C', '9'), ('C', '8'), ('C', '7'), ('C', '6'), ('C', '5'), ('C', '4'), ('C', '3'), ('C', '2'), ('C', 'ACE'), ('H', 'JOKER'), ('H', 'KING'), ('H', 'QUEEN'), ('H', 'JACK'), ('H', '10'), ('H', '9'), ('H', '8'), ('H', '7'), ('H', '6'), ('H', '5'), ('H', '4'), ('H', '3'), ('H', '2'), ('H', 'ACE')]
    assert len(deck.deck) == 70

def test_shuffle_deck(deck):
    deck.shuffle_deck()
