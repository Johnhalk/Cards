import pytest
from value import Value

@pytest.fixture
def value():
    '''Creates new instance of value class.'''
    return Value()

def test_value_initialisation(value):
    assert value.value == ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']


def test_add_value(value):
    value=Value()
    value.add_value('Joker')
    assert value.value == ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'JOKER']

def test_add_value_two(value, capfd):
    value.add_value('ACE')
    out, err = capfd.readouterr()
    assert out == "Value already exists.\n"

def test_delete_value(value):
    value.delete_value('2')
    assert value.value == ['ACE', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

def test_delete_suit_two(value, capfd):
    value.delete_value('Joker')
    out, err = capfd.readouterr()
    assert out == "Not a valid value.\n"
