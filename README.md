# Chess
![GitHub](https://img.shields.io/github/license/AhmedAlzubairi1/COMS4995?style=plastic)
[![Build Status](https://travis-ci.org/AhmedAlzubairi1/Chess.svg?branch=master)](https://travis-ci.org/AhmedAlzubairi1/Chess)
![Codecov](https://img.shields.io/codecov/c/github/AhmedAlzubairi1/Chess)
[![Docs](https://img.shields.io/readthedocs/chess.svg)](https://chess1.readthedocs.io)

COMS4995 Project -> Chess Backend


This is repo for a chess backend that you can use for your chess game. All you need to do is to handle the front end. Everything else such as the rules of the game and movement is already handled by the backend. 


To run the sample terminal front end of the game do : 
python Game/terminalGame.py

When playing the game. This is how you move a piece:
If you want to move a piece at 1A to 3B, just type : 1A to 3B
The game would shift between players so that each player gets a turn until someone wins. 


When creating your frontend, you would need to copy the logic in the terminalGame.py file. Specifically you need to use the initGame, function to start the game. THen you can use whatever frontend you want to make the chess game.
