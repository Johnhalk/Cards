## Deck of Cards programme
![Imgur](http://imgur.com/uAiB32I.png)

## Core features of task:

- There are four suits: Hearts, Clubs, Spades and Diamonds.
- There are thirteen values: Ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
- There will be one deck of 52 cards
- There will be four players
- The deck arrives in perfect sequence (ace of hearts at the bottom, two next etc. with the King of diamonds at the top)
-  Shuffle the cards  - We would like to take the deck that is in sequence and shuffle it so that no two cards are still in sequence.
-  Deal the cards - We would then like to deal seven cards to each player (one card to the each player, then a second card to each player, and so on.

## User Stories

```

As a player,
So that I can see what suits I have,
I want to be able to see what suits are in play.

As a player,
So that I can see the range of values,
I want to be able to see how many values there are.

As a player,
So that I can see my cards,
I want to be able to create cards made up of each suit and value combination possible.

As a player,
So that I can understand my deck,
I want to be able to create a deck comprised of cards that are of each value and suit available.

As a player,
So that I can play successfully,
I want to be able to deal to all players playing.

As a player,
So that I can use my deck,
I want my deck to perfectly ordered.

As a player,
So I can play the game,
I want there to be minimum four players in the game.

As a player,
So that I can use my deck fairly,
I want to shuffle all cards in my deck so they are in random order and no two cards are still in sequence.

As a player,
So that I can deal to players,
I would like to be able to deal 7 cards to each player, one at a time.

```

## Technologies and Dependencies

**Core**
- Python
- Pip
- Pytest

**Testing**

- Pytest
- Pytest-cov


## Installation and Usage

- If received via a zip file, load it from the desired file location saved on your computer.

- This programme is run directly off the command line. To open your preferred command-line interface look at the instructions below:

- **Windows**
Go to Start menu → All Programs → Accessories → Command Prompt.
- **OS X**
Go to Applications → Utilities → Terminal.
- **Linux**
Go to Applications → Accessories → Terminal.

- This programme is written in Python, download Python for your computer below:
- [Windows](https://www.python.org/downloads/windows/)
- [Mac OS](https://www.python.org/downloads/release/python-351/)
- **Linux**
It is very likely Linux has Python already installed.

- To check you installed it correctly type the following into the command-line:
```
$ python3 --version
Python 3.5.1 (this should be the output)
```

- Install pip
- Install pytest
- Install pytest-cov

## File architecture design choice:

![Imgur](http://imgur.com/7UvxxuQ.png)

**suit.py**

The suit class has their own state and is initialised with the suits H, C, D, S - the four necessary to play our game. However there are more possible suits that can be added past the initial four and used in other games that could be created which is why logically suits have their own class.

**value.py**

Similarly to suit, the value class has their own state and is initialised with the values ACE, 2, .. , KING - the values necessary to play our game. However there are more possible values that can be added past the initial values and used in other games that could be created which is why logically value have their own class.

**card.py**

The card class is initialised by inheriting both a suit class and a value class. Logically cards both have suits and values.  Based upon the values and suits available all possible card combinations exist.

**deck.py**

The deck class is initialised by inheriting a card class and uses the cards to form the 52 card deck needed for the game and the decks own functionality.

**game.py**

The game class is initialised by inheriting directly from a deck class and a player class.  A game needs a deck and needs players to function.

**player.py**

The player class does not inherit from game.  It is its sole entity.  A player can exist and there can be many but they do not necessarily have a game to be paired with.

##Detailed explanation of each class file:

**suit.py**
```
class Suit(object):

    def __init__(self):
        self.suit = ['H', 'C', 'S', 'D']


    def add_suit(self, suit_type):
        if suit_type.upper() not in self.suit:
            self.suit.append(suit_type.upper())
        else:
            print "Suit already exists."

    def delete_suit(self, suit_type):
        if suit_type.upper() in self.suit:
            self.suit.remove(suit_type.upper())
            return self.suit
        else:
            print "Not a valid suit."
```

- When an instance of suit is created it is initialised with H, C, S, D (Hearts, Clubs, Spades, Diamonds.).  The four suits necessary for the game.

- Methods to add more suits or delete more suits (add_suit and delete suit respectively) are added to the file too. This is to expand on any future games that may not require all four suits, or any games that require more.

Feature test for necessary requirements - suits are of H, C, S, D:
- Run from the command-line.
```
python
execfile('lib/suit.py')
suit=Suit()
suit.suit
exit()
```
Feature tests for extra functionality:
- Run from the command-line.
```
python
execfile('lib/suit.py')
suit=Suit()
suit.suit
suit.add_suit('T')
suit.add_suit('T')
suit.suit
suit.delete_suit('T')
suit.delete_suit('T')
suit.suit
exit()
```

**value.py**

```
class Value(object):
    def __init__(self):
        self.value = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']


    def add_value(self, value_type):
        if value_type.upper() not in self.value:
            self.value.append(value_type.upper())
        else:
            print "Value already exists."

    def delete_value(self, value_type):
        if value_type.upper() in self.value:
            self.value.remove(value_type.upper())
            return self.value
        else:
            print "Not a valid value."
```

- When an instance of value is created it is initialised with values ACE, 2, ... , KING.  The values necessary for our game.

- Methods to add more or delete more values(add_value and delete_value respectively) are added to the file too. This is to expand on any future games that may not require all values, or may require more.

Feature test for necessary requirements - values are of Ace, 2, ... , KING:
- Run from the command-line.
```
python
execfile('lib/value.py')
value=Value()
value.value
exit()
```

Feature test for extra functionality:
- Run from the command-line.
```
python
execfile('lib/value.py')
value=Value()
value.value
value.add_value('Joker')
value.add_value('Joker')
value.value
value.delete_value('Joker')
value.delete_value('Joker')
value.value
exit()
```

**card.py**

```

class Card(Suit, Value):

    def __init__(self):
        Suit.__init__(self)
        Value.__init__(self)
        self.card_list = list(itertools.product(self.suit, self.value))

    def create_card_list(self):
        self.card_list = list(itertools.product(self.suit, self.value))

    def amount_of_cards(self):
        print "The amount of cards are:", len(self.card_list)

    def add_new_suit(self, suit_type):
        self.add_suit(suit_type)
        self.create_card_list()

    def add_new_value(self, value_type):
        self.add_value(value_type)
        self.create_card_list()

    def delete_existing_suit(self, suit_type):
        self.delete_suit(suit_type)
        self.create_card_list()
        return self.card_list

    def delete_existing_value(self, value_type):
        self.delete_value(value_type)
        self.create_card_list()
        return self.card_list

    def create_singular_card(self, suit_type, value_type):
        self.card_list.append((suit_type.upper(), value_type.upper()))

    def delete_singular_card(self, suit_type, value_type):
        self.card_list.remove((suit_type.upper(), value_type.upper()))

```

- When an instance of card is created it initialises with both suit and value. Then using Pythons built in itertools it creates a product of all possible combinations saved to an instance variable self.card_list.

- In the card class there is added functionality to add new suits and values, delete existing suits and values and create singular types of cards (Good for creating a Joker perhaps?).  Created so the code can be expanded on should any games require more card types.

Feature test for necessary requirements - there should be 52 cards.
- Run from the command-line.
```
python
execfile('lib/card.py')
card=Card()
card.card_list
len(card.card_list)
exit()
```

Feature test for additional functionality:
- Run from the command-line.
```
python
execfile('lib/card.py')
card=Card()
card.card_list
len(card.card_list)
card.amount_of_cards()
card.add_new_suit('kg')
card.add_new_suit('KG')
card.add_new_value('Shoes')
card.add_new_value('SHOES')
card.card_list
len(card.card_list)
card.delete_existing_suit('h')
card.delete_existing_suit('H')
card.suit
card.card_list
card.delete_existing_value('2')
card.delete_existing_value('2')
card.value
card.card_list
card.create_singular_card('KG','Shoes')
card.card_list
len(card.card_list)
card.delete_singular_card('D', '5')
card.card_list
len(card.card_list)
exit()
```

**deck.py**

```
class Deck(Card):

    def __init__(self, shuffled=False):
        Card.__init__(self)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.shuffled = shuffled

    def show_deck(self):
        print "The deck is comprised of:", self.deck

    def add_new_card_type(self, suit_type, value_type):
        self.add_new_suit(suit_type)
        self.add_new_value(value_type)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.show_deck()

    def delete_card_type(self, suit_type, value_type):
        self.delete_existing_suit(suit_type)
        self.delete_existing_value(value_type)
        self.deck = list(reversed(self.card_list))
        self.shuffle_deck_compare = list(self.deck)
        self.show_deck()

    def create_singular_card_to_deck(self, suit_type, value_type):
        self.create_singular_card(suit_type, value_type)
        self.deck = list(reversed(self.card_list))

    def delete_singular_card_from_deck(self, suit_type, value_type):
        self.delete_singular_card(suit_type, value_type)
        self.deck = list(reversed(self.card_list))

    def shuffle_deck(self):
        random.shuffle(self.deck)
        i=0
        n=0
        while i < (len(self.deck) -1) and n < (len(self.deck) -1):
            if (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) == (self.deck[n], self.deck[n+1]):
                print "Reshuffling..."
                self.shuffle_deck()
            elif (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) != (self.deck[n], self.deck[n+1]) and n < (len(self.deck) -1):
                n+=1
            elif (self.shuffle_deck_compare[i], self.shuffle_deck_compare[i+1]) != (self.deck[n], self.deck[n+1]) and n == (len(self.deck) -1):
                i+=1
                n=0
            else:
                return
        else:
            self.shuffled = True
            return self.deck
```

- When an instance of deck class is created it initialises card. To meet the acceptance criteria the deck must arrive in perfect sequence (so, ace of hearts is at the bottom, two of hearts is next, etc. all the way up to king of diamonds on the top).  The card class initialises the cards the opposite way as required hence an instance variable is assigned (self.deck) to the reverse list of the card_list and meeting the criteria.

- A deck is initialised as not shuffled, to avoid a game starting without shuffling == True.

- The other acceptance criteria: Shuffle the cards - We would like to take the deck that is in sequence and shuffle it so that no two cards are still in sequence. Means no two cards can remain in sequence after a shuffle - e.g. for a perfectly sequenced(as explained above) deck this means nowhere in the deck can two cards still be in sequence - e.g. 5 of hearts can not be before a 4 of hearts anywhere even after shuffling.  This applies for all card sequencing.

Initially I used the .random method to randomise but this never met the criteria.  Then I considered splitting a deck into two halves of odd and even indexes then merging the odd index half and even index half back into one deck.  This however eliminated all chances of randomness and made the card order too predictable (got to stop card counting!)

I then


##Quick feature test run:

- Start the Python interactive interpreter. The Python interpreter can be invoked by typing the command "python" into the command-line interface followed by the "return" key
- **Type this into terminal:**
```
python
```

- Next we need to load the file directly into the interactive interpreter. Type execfile('game.py') Here you will have loaded up the game and logic to play.
- **Type this into terminal:**
```
execfile('game.py')
```

- Below runs the entire game, copy and paste into the terminal for a fast demonstration of the game running - game=Game() creates a new instance of game

```

```

## To Do List ##

Add both feature tests and unit tests for each individual class file as well as an overall one for game class to run code for user.

Add method to deck class to create a new card to add to deck.
Add similar to game?
Add more user stories
## Testing

install Pip with this command on the command line
```
sudo easy_install pip
```
if you get an error run
```
sudo chown -R $USER /Library/Python/2.7
```

Then run the following:
```
sudo easy_install pip.
sudo easy_install virtualenv.
sudo easy_install pytest
```


## Shuffle a deck of cards!
Initial thoughts:

```
def __init__(self, shuffled=False):
    Card.__init__(self)
    self.deck = self.card_list
    self.shuffle_deck_compare = list(self.card_list)
    self.shuffled = shuffled

def shuffle_deck(self):
    random.shuffle(self.deck)
    i=0
    while i < (len(self.deck) -1):
        if self.shuffle_deck_compare[i] == self.deck[i]:
            self.shuffle_deck()
            i+=1
        else:
            self.shuffled = True
            return self.card_list
```
