# Star Wars Top Trumps Battle Mat with Computer Vision and AI

Rules for Phase 1-type game.

## Why

That game is developed on my spare time, so I must use an incremental approach to getting things in order. Phase 1 is a simplified version of the original game; there will be several phases, each one adding complexity until the whole rulebook is integrated into this program.

## Legal

Star Wars Top Trumps Battle Mat is not my intellectual property. TOP TRUMPS is a registered trademark of Winning Moves UK Ltd. You need to buy a box of the game in order to use that software. That software is not supported in any way by the owner of the game. The original game is sold in stores and is copyrighted by Winning Moves UK Limited (2023).

## How to run Phase 1

```
python3 ./tt-sw-bm-phase1.py
```

## Glossary

#### QR-cam

To QR-cam a card is to show the QR code printed on it to the webcam of the computer against which you're playing.
It is a way for the AI to keep track of the state of the battle. As a rule of thumb, QR-cam every card you take from the deck. The AI won't know which cards you have in hand unless you pick the Grand Master difficulty level.

#### Human Player & Computer Player

Human Player is Player 1, the human player. Computer Player is the computer.

#### Rounds, Battles

A round is made of the comparison of two cards.
A battle is made of 3 rounds.
Whoever wins 7 battles 1st is considered as victorious.

## Stages and steps

### Init

This stage is there to determine who will get the initiative.

- Shuffle the deck
- Human Player draws 1 card from the deck and QR-cams it
- Computer Player draws 1 card from the deck and QR-cams it
- The AI compares the Top Trumps Galactic Legend category of both cards. If Human Player TTGL > Computer Player TTGL then Human Player has initiative. If Computer Player TTGL > Human Player TTGL then Computer Player has initiative. If both values are equal, discard cards, redraw and compare again.
- Return the cards to the deck
- Shuffle the deck

### Start

- Human Player draws 3 cards from the deck and QR-cams it
- Computer Player draws 3 cards from the deck and QR-cams it

### Loop

If Human Player has initiative, he plays 1st, otherwise, Computer Player does.

- Player X picks 1 card from hand and places it in a category of his choice
- Player Y picks 1 card from hand and places it in the same category
- Compare: Highest wins the round and places the 2 cards in the Scoring space
- Invert Player X and Y
- Repeat steps above twice (there are 3 rounds in each battle)
- Once you went through 3 rounds, go back to Start and play again
- Game ends when someone wins 7 battles

### End

First player to win 7 battles is victorious.

