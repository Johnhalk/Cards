import pytest
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))
from card import Card

@pytest.fixture
def card():
    '''Creates new instance of card class'''
    return Card()

def test_card_initialisation(card):
    assert card.suit == ['H', 'C', 'S', 'D']
    assert card.value == ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('H', 'KING'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING')]

def test_create_card_list(card):
    card.card_list
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('H', 'KING'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING')]

def test_amount_of_cards(card, capfd):
    card.amount_of_cards()
    out, err = capfd.readouterr()
    assert out == "The amount of cards are: 52\n"

def test_add_new_suit(card, capfd):
    card.add_new_suit('H')
    out, err = capfd.readouterr()
    assert out == "Suit already exists.\n"
    assert card.suit == ['H', 'C', 'S', 'D']

def test_add_new_suit_two(card):
    card.add_new_suit('T')
    assert card.suit == ['H', 'C', 'S', 'D', 'T']
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('H', 'KING'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING'), ('T', 'ACE'), ('T', '2'), ('T', '3'), ('T', '4'), ('T', '5'), ('T', '6'), ('T', '7'), ('T', '8'), ('T', '9'), ('T', '10'), ('T', 'JACK'), ('T', 'QUEEN'), ('T', 'KING')]

def test_add_new_value(card, capfd):
    card.add_new_value('Ace')
    out, err = capfd.readouterr()
    assert out == "Value already exists.\n"
    assert card.value == ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

def test_add_new_value_two(card):
    card.add_new_value('Joker')
    assert card.value == ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'JOKER']
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('H', 'KING'), ('H', 'JOKER'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('C', 'JOKER'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('S', 'JOKER'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING'), ('D', 'JOKER')]

def test_delete_existing_suit(card):
    card.delete_existing_suit('H')
    assert card.suit == ['C', 'S', 'D']

def test_delete_existing_suit_two(card, capfd):
    card.delete_existing_suit('T')
    out, err = capfd.readouterr()
    assert out == 'Not a valid suit.\n'

def test_delete_existing_value(card):
    card.delete_existing_value('3')
    assert card.value == ['ACE', '2', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

def test_delete_existing_value_two(card, capfd):
    card.delete_existing_value('Joker')
    out, err = capfd.readouterr()
    assert out == 'Not a valid value.\n'

def test_create_singular_card(card):
    card.create_singular_card('','Joker')
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('H', 'KING'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING'), ('', 'JOKER')]

def test_delete_singular_card(card):
    card.delete_singular_card('H','King')
    assert card.card_list == [('H', 'ACE'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '10'), ('H', 'JACK'), ('H', 'QUEEN'), ('C', 'ACE'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '10'), ('C', 'JACK'), ('C', 'QUEEN'), ('C', 'KING'), ('S', 'ACE'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '10'), ('S', 'JACK'), ('S', 'QUEEN'), ('S', 'KING'), ('D', 'ACE'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '10'), ('D', 'JACK'), ('D', 'QUEEN'), ('D', 'KING')]
