from sys import path
from os.path import dirname as dir
path.append(dir(path[0])[0:dir(path[0]).rfind('\\')])
from  Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook
# Make sure to appending c:\Users\Ahmed Alzubairi\Documents\Open Source\COMS4995

def test_pawn_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Pawn(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="3A"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_pawn_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Pawn(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,3,'B')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="3B"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0

def test_bishop_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Bishop(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4C"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_bishop_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Bishop(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,4,'C')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4C"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0

def test_rook_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Rook(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="8A"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_rook_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Rook(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,8,'A')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="8A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0

def test_knight_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Knight(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4B"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_knight_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Knight(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,4,'B')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4B"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0

def test_queen_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Queen(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4A"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    moveOne="4A"
    moveTwo="4D"
    #Now I make a second move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_queen_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=Queen(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,4,'D')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="4A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    moveOne="4A"
    moveTwo="4D"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0


def test_king_move():
    playerOnePieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=King(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="3A"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    moveOne="3A"
    moveTwo="3B"
    #Now I make a second move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
def test_king_capture():
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    color="BLACK"
    myPiece=King(board,color,playerOnePieces,2,'A')
    playerOnePieces.update({myPiece})
    enemyPiece=Pawn(board,"WHITE",playerTwoPieces,3,'B')
    playerTwoPieces.update({enemyPiece})
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
    moveOne="2A"
    moveTwo="3A"
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    moveOne="3A"
    moveTwo="3B"
    #Now I make a move
    board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
    
    assert board[possibleRow[int(moveTwo[0])]][possibleCol[moveTwo[1]]] == myPiece
    assert len(playerTwoPieces) == 0





