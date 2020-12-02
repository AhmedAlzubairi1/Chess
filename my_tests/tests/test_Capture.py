from Game.Pieces.Rook import Rook
from Game.Pieces.Queen import Queen
from Game.Pieces.Pawn import Pawn
from Game.Pieces.Knight import Knight
from Game.Pieces.King import King
from Game.Pieces.Bishop import Bishop
from Game.Game import Game
# from sys import path
# from os.path import dirname as dir
# path.append(dir(path[0])[0:dir(path[0]).rfind('\\')])
# Make sure to appending c:\Users\Ahmed Alzubairi\Documents\Open
# Source\COMS4995


def test_pawn_capture():
    """Tests if pawn can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Pawn(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 3, 'B', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "3B"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_bishop_capture():
    """Tests if bishop can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Bishop(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'C', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4C"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_rook_capture():
    """Tests if rook can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Rook(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 8, 'A', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "8A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_knight_capture():
    """Tests if the knight can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Knight(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'B', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4B"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_queen_capture():
    """Tests if the queen can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Queen(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'D', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    moveOne = "4A"
    moveTwo = "4D"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])

    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_king_capture():
    """Tests if the king can capture
    """
    myGame = Game()
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = King(board, color, playerOnePieces, 2, 'A', myGame)
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 3, 'B', myGame)
    playerTwoPieces.update({enemyPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "3A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    moveOne = "3A"
    moveTwo = "3B"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])

    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0
