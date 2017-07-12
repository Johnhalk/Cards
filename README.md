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
