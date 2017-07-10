## Deck of Cards programme
![Imgur](http://imgur.com/uAiB32I.png)

## Core features

- There are four suits: Hearts, Clubs, Spades and Diamonds.
- There are thirteen values: Ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
- There will be one deck of 52 cards
- There will be four players
- The deck will be created in perfect sequence (ace of hearts at the bottom, two next etc. with the King of diamonds at the top)
-  The deck can be shuffled and have the cards be in a total random order.
-  The cards can be dealt to each player, one card at a time to each player, until each player has 7 cards.

## User Stories

```

As a card dealer,
So that I can see what suits I have,
I want to be able to see what suits are in play.

As a card dealer,
So that I can see the range of values,
I want to be able to see how many values there are.

As a card dealer,
So that I can see my cards,
I want to be able to create cards made up of each suit and value combination possible.

As a card dealer,
So that I can understand my deck,
I want to be able to create a deck comprised of each value and suit available.

As a card dealer,
So that I can deal successfully,
I want to be able to deal to all players playing.

As a card dealer,
So that I can use my deck,
I want my deck to perfectly ordered when created.

As a card dealer,
So that I can use my deck fairly,
I want to shuffle all cards in my deck so they are in random order.

As a card dealer,
So that I can deal to players,
I would like to be able to deal 7 cards to each player, one at a time.

```

## Technologies and Dependencies

**Core**


**Testing**



## Installation and Usage

- This is run off of the Command Line. To start please type 'python'
- Type execfile('game.py') Here you will have loaded up the game and logic to play.

```
execfile('game.py')
game=Game()
game.add_player('P1', 'John')
game.add_player('P2', 'KG')
game.add_player('P3', 'Eammon')
game.add_player('P4', 'Jane')
game.deck
game.prepare_game()
game.deal_one_card_per_player()
game.show_hands()
game.deal_one_card_per_player()
game.show_hands()
game.deck
game.deal_game()
game.show_hands()
```

## To Do List ##

Add both feature tests and unit tests for each individual class file as well as an overall one for game class to run code for user.

Add method to deck class to create a new card to add to deck.
Add similar to game?

## Testing
