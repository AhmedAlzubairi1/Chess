# Chess
![GitHub](https://img.shields.io/github/license/AhmedAlzubairi1/COMS4995?style=plastic)
[![Build Status](https://travis-ci.org/AhmedAlzubairi1/Chess.svg?branch=master)](https://travis-ci.org/AhmedAlzubairi1/Chess)
[![codecov](https://codecov.io/gh/AhmedAlzubairi1/Chess/branch/master/graph/badge.svg?token=37GQ0IOMUG)](https://codecov.io/gh/AhmedAlzubairi1/Chess)
[![Documentation Status](https://readthedocs.org/projects/chess1/badge/?version=latest)](https://chess1.readthedocs.io/en/latest/?badge=latest)

Personal Website:
https://ahmedalzubairi1.github.io/ahmedalzubairi.github.io/

# COMS4995 Project -> Chess Backend

This is a chess backend repo that you can use for your front end chess implementation. The code handles everything about the the game, such as the rules, captures, movements, ect. All you have to do is handle the display. By default, the repo has a terminal front end that you can interact with. Here is a demo of how the game looks like using the terminal front end: 
![](demo.gif)


## Installation
There isn't any package manager to install the repo. The way to install the repo is to just fork/clone it. 


## Running the Game

To run the sample terminal front end of the game do : 

```
cd Game
python gameRunner.py
```

## Features
- Creates a Chess Board
- Has all Chess Pieces
- Ability to move pieces
- Ability to capture pieces
- Castling 
- Pawn Passant capture
- Checks
- Check Mates

## Documentation
- [Read the Docs](https://chess1.readthedocs.io/en/latest/) is where you will find a detailed explanation of what each method/function does


When playing the game. This is how you move a piece:
If you want to move a piece at 1A to 3B, just type : 1A to 3B
The game would shift between players so that each player gets a turn until someone wins. 


When creating your frontend, you would need to copy the logic in the terminalGame.py file. Specifically you need to use the initGame, function to start the game. THen you can use whatever frontend you want to make the chess game.

To run the game on the terminal front end, go to the Game directory and run the python script gameRunner.py as such:

```
cd Game
python gameRunner.py
```
Follow the instructions to move pieces. First to get a check mate wins.
To demo The chess engine on the front end w/ terminal interface:
![](demo.gif)
