## Deck of Cards programme
![Imgur](http://imgur.com/uAiB32I.png)

## Introduction
This programme is created in Python. A language I have self-taught myself while outside of Makers Academy.

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

## Quick feature run down to show functionality:

**Deck arrives to game in perfect sequence, with all 52 card combinations of the suits and values.**
- Type into the command line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
exit()
```

**Deck shuffles for the game so no two cards are still in sequence**
- Type into command line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
game.add_player('Kurt')
game.add_player('Gieger')
game.add_player('Shoes')
game.add_player('John')
game.start_game()
game.players[0].hand
len(game.players[0].hand)
game.players[1].hand
len(game.players[1].hand)
game.players[2].hand
len(game.players[2].hand)
game.players[3].hand
len(game.players[3].hand)
exit()
```

**Game can deal cards one at a time to each player**
- Type into command-line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
game.add_player('Kurt')
game.add_player('Gieger')
game.add_player('Shoes')
game.start_game()
game.add_player('John')
game.start_game()
game.players[0].hand
len(game.players[0].hand)
game.players[1].hand
len(game.players[1].hand)
game.players[2].hand
len(game.players[2].hand)
game.players[3].hand
len(game.players[3].hand)
game.start_game()
len(game.players[0].hand)
len(game.players[1].hand)
len(game.players[2].hand)
len(game.players[3].hand)
exit()
```

## Detailed explanation of each class file:

## suit.py
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

- **Acceptance criteria: There must be 4 suits** When an instance of suit is created it is initialised with H, C, S, D (Hearts, Clubs, Spades, Diamonds.).  The four suits necessary for the game.

Feature test for necessary requirements - suits are of H, C, S, D:
- Run from the command-line.
```
python
execfile('lib/suit.py')
suit=Suit()
suit.suit
exit()
```

- Methods to add more suits or delete more suits (add_suit and delete suit respectively) are added to the file too. This is to expand on any future games that may not require all four suits, or any games that require more.

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

## value.py

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

- **Acceptance criteria: There must be 13 values** When an instance of value is created it is initialised with values ACE, 2, ... , KING.  The values necessary for our game.

Feature test for necessary requirements - values are of Ace, 2, ... , KING:
- Run from the command-line.
```
python
execfile('lib/value.py')
value=Value()
value.value
exit()
```

- Methods to add more or delete more values(add_value and delete_value respectively) are added to the file too. This is to expand on any future games that may not require all values, or may require more.

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

## card.py

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

- **Acceptance criteria: 52 cards** When an instance of card is created it initialises with both suit and value. Then using Pythons built in itertools it creates a product of all possible combinations saved to an instance variable self.card_list.

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

- In the card class there is added functionality to add new suits and values, delete existing suits and values and create singular types of cards (Good for creating a Joker perhaps?).  Created so the code can be expanded on should any games require more card types.

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

## deck.py

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

- **Acceptance criteria: The deck arrives in perfect sequence (so, ace of hearts is at the bottom, two of hearts is next, etc. all the way up to king of diamonds on the top).** When an instance of deck class is created it initialises card. To meet the acceptance criteria the deck must arrive in perfect sequence (so, ace of hearts is at the bottom, two of hearts is next, etc. all the way up to king of diamonds on the top).  The card class initialises the cards the opposite way as required hence an instance variable is assigned (self.deck) to the reverse list of the card_list and meeting the criteria.

Feature test for necessary requirements - deck in perfect sequence:
- Run from the command-line:
```
python
execfile('lib/deck.py')
deck=Deck()
deck.deck
len(deck.deck)
exit()
```
- A deck is initialised as not shuffled, to avoid a game starting without shuffling == True.

- **Acceptance criteria: Shuffle the cards - We would like to take the deck that is in sequence and shuffle it so that no two cards are still in sequence.** This meant no two cards can remain in sequence after a shuffle - e.g. for a perfectly sequenced(as explained above) deck this means nowhere in the deck can two cards still be in sequence - e.g. 5 of hearts can not be before a 4 of hearts anywhere even after shuffling.  This applies for all card sequencing for a perfectly sequenced deck.

Initially I used the .random method to randomise but this never met the criteria.  Then I considered splitting a deck into two halves of odd and even indexes then merging the odd index half and even index half back into one deck.  This however eliminated all chances of randomness and made the card order too predictable (got to stop card counting!)

To counter this I created a clone of a deck that would be created upon initialisation. saved as an instance variable: self.shuffle_deck_compare. Using the random.shuffle() method built into Python on self.deck to randomise the card order I then used a while statement that allowed me to check over each pair of element indexes that no two indexes in the newly shuffled self.deck matched that of the "copy" deck self.shuffle_deck_compare! It would check over each element in the list(array) and if the boolean condition returned False it would continue down the list and increment the element it was checking.  This covered all possible chances of the deck returning two sequenced elements somewhere in the deck.  Of course if it found a matching element it would just instantly reshuffle the deck and continue until it didn't.  This would then set self.shuffled == True and return a newly shuffled deck ready for a game to be played!

Feature test for necessary requirements - Shuffle the cards  - We would like to take the deck that is in sequence and shuffle it so that no two cards are still in sequence
- Run from the command-line:
```
python
execfile('lib/deck.py')
deck=Deck()
deck.deck
deck.shuffle_deck_compare
deck.shuffle_deck()
deck.deck
deck.shuffle_deck()
deck.deck
deck.shuffle_deck_compare
exit()
```

- Similar to the card class, the deck can also add and delete card types as well as create and delete singular ones for a deck.

Feature test for additional functionality:

```
python
execfile('lib/deck.py')
deck=Deck()
deck.deck
len(deck.deck)
deck.shuffle_deck()
deck.add_new_card_type('KG','Shoe')
deck.delete_card_type('H','5')
deck.create_singular_card_to_deck('','Joker')
deck.deck
deck.delete_singular_card_to_deck('H','Ace')
deck.deck
deck.shuffle_deck()
exit()
```

## game.py

```
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
```

- **Acceptance criteria : The deck arrives in perfect sequence** When an instance of deck is created it initialises with a fully sequenced playable deck, unshuffled and an empty player list(array).

Feature test for deck arriving in perfect sequence:
- Run from the command-line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
exit()
```

- **Acceptance criteria : 4 players must be waiting in the game.** Players can be added to a game using the add_player method which adds the newly created player class into an instance variable of the game self.players.  There is currently no maximum to how many players can be added to a game.  The game can not start until there are at least four players.  This is requirement is in the code as a global variable declared outside of the game class. currently "MIN_NUMBER_OF_PLAYERS_REQUIRED = 4".  This design choice has been made because minimum players necessary may easily change and we only need to change the global variable rather than every bit of our code.

Feature test for four players being at table:
- Run from the command-line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
game.add_player('Kurt')
game.add_player('Gieger')
game.add_player('Shoes')
game.start_game()
game.add_player('John')
game.start_game()
game.players[0].hand
len(game.players[0].hand)
game.players[1].hand
len(game.players[1].hand)
game.players[2].hand
len(game.players[2].hand)
game.players[3].hand
len(game.players[3].hand)
exit()
```

- **Acceptance criteria : Deal the cards - We would then like to deal seven cards to each player (one card to the each player, then a second card to each player, and so on).**  A global variable is declared as: "MAX_START_OF_HAND = 7" and used to check the length of each players hand.  This allows me to modify how many cards a player starts with without editing all of the code.  I use a while loop in the deal_one_card_per_player method that pops a card from a deck into the player class's hand.

Feature test for each player only receiving 7 cards in hand -
- Ran in command-line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
game.add_player('Kurt')
game.add_player('Gieger')
game.add_player('Shoes')
game.start_game()
game.add_player('John')
game.start_game()
game.players[0].hand
len(game.players[0].hand)
game.players[1].hand
len(game.players[1].hand)
game.players[2].hand
len(game.players[2].hand)
game.players[3].hand
len(game.players[3].hand)
game.start_game()
len(game.players[0].hand)
len(game.players[1].hand)
len(game.players[2].hand)
len(game.players[3].hand)
exit()
```

- Players can also be removed from a game.

Feature test to show added functionality:
- Ran in command-line:
```
python
execfile('lib/game.py')
game=Game()
game.deck
game.add_player('Kurt')
game.add_player('Gieger')
game.players[0].name
game.players[1].name
game.remove_player(1)
game.players[0].name
game.players
exit()
```

## player.py

```
class Player(object):

    def __init__(self, name):
        self.name = name.upper()
        self.hand = []

    def who_am_i(self):
        print "You are" , self.name

    def my_hand(self):
        print "Your hand is:", self.hand
```

- The player class does not inherit from anythin.  A player can exist but does not necessarily need a game.
- For the subject of card games players have hands and initialise with a hand.
- Players also need a name to identify in games and initialise with a name.

Feature test to show functionality:
- Ran in command-line:
```
python
execfile('lib/player.py')
player=Player('John')
player.name
player.hand
player.who_am_i()
player.my_hand()
exit()
```
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

- There are 48 tests in total, all passing:
![Imgur](http://imgur.com/raNLo6a.png)

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

## The future....?

- I would like to adapt the programme's current form and make it usable for other kind of games.  There is currently one game class, however no one game is alike.  There could be plenty of games with different rules that inherit from the foundations of the deck of cards created.  

- I would like to expand on the current games rules.  Currently all it does is exist and deal cards, not exactly the most engaging of games!

- Look to creating a dealer class which controls the flow of a game.

- look to create a table class in case there are requirements for placements of cards in specific games.

- expand the programme into a front end model with graphics and styling.
