from Game.Pieces.Rook import Rook
from Game.Pieces.Queen import Queen
from Game.Pieces.Pawn import Pawn
from Game.Pieces.Knight import Knight
from Game.Pieces.King import King
from Game.Pieces.Bishop import Bishop
# from sys import path
# from os.path import dirname as dir
# path.append(dir(path[0])[0:dir(path[0]).rfind('\\')])
# Make sure to appending c:\Users\Ahmed Alzubairi\Documents\Open
# Source\COMS4995


def test_sample():
    x = Bishop([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    x = Queen([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    x = King([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    x = Knight([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    x = Rook([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    x = Pawn([[1, 2, 3], [4, 5, 6]], 'BLACK', set(), 1, 'A', [])
    print(x)

    assert 1 == 1


'''
def test_pawn_move():
    """Tests if the pawn can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Pawn(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "3A"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_pawn_capture():
    """Tests if pawn can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Pawn(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 3, 'B')
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


def test_bishop_move():
    """Tests if bishop can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Bishop(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4C"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_bishop_capture():
    """Tests if bishop can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Bishop(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'C')
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


def test_rook_move():
    """Tests if rook can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Rook(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "8A"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_rook_capture():
    """Tests if rook can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Rook(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 8, 'A')
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


def test_knight_move():
    """Tests if the knight can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Knight(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4B"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_knight_capture():
    """Tests if the knight can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Knight(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'B')
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


def test_queen_move():
    """Tests if the queen can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Queen(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "4A"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    moveOne = "4A"
    moveTwo = "4D"
    # Now I make a second move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_queen_capture():
    """Tests if the queen can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = Queen(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 4, 'D')
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


def test_king_move():
    """Tests if the king can move
    """
    playerOnePieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = King(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    possibleRow = {i: i - 1 for i in range(1, 9)}
    possibleCol = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + 8)}
    moveOne = "2A"
    moveTwo = "3A"
    # Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    moveOne = "3A"
    moveTwo = "3B"
    # Now I make a second move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(
        int(moveTwo[0]), moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]
                 ][possibleCol[moveTwo[1]]] == myPiece


def test_king_capture():
    """Tests if the king can capture
    """
    playerOnePieces = set()
    playerTwoPieces = set()
    board = [[None] * 8 for i in range(8)]
    color = "BLACK"
    myPiece = King(board, color, playerOnePieces, 2, 'A')
    playerOnePieces.update({myPiece})
    enemyPiece = Pawn(board, "WHITE", playerTwoPieces, 3, 'B')
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
'''
