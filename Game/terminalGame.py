'''
NO LONGER SHOULD USE THIS CLASS, MAKE SURE TO DELETE BEFORE RELEASING VERSION 1
'''

from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from  Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook
print(11)
def initPlayerOne(playerOnePieces,board):
    """This populates the playerOnePieces (black) empty set with the player one's pieces. It also adds those pieces to the board

    :param playerOnePieces: An empty set representing player one's pieces
    :type playerOnePieces: set
    :param board: A 2d list consisting of an 8 by 8 None objects and any prepopulated pieces
    :type board: [list]
    """    
    #add pawns
    #(self,board,color,group,row,col)
    color="BLACK"
    group=playerOnePieces
    playerOnePieces.update({Pawn(board,color,group,2,'A'),Pawn(board,color,group,2,'B'),Pawn(board,color,group,2,'C'),Pawn(board,color,group,2,'D'),Pawn(board,color,group,2,'E'),Pawn(board,color,group,2,'F'),Pawn(board,color,group,2,'G'),Pawn(board,color,group,2,'H')})

    #Add rank 1 pieces
    playerOnePieces.update({Rook(board,color,group,1,'A'),Knight(board,color,group,1,'B'),Bishop(board,color,group,1,'C'),Queen(board,color,group,1,'D'),King(board,color,group,1,'E'),Bishop(board,color,group,1,'F'),Knight(board,color,group,1,'G'),Rook(board,color,group,1,'H')})
    
def initPlayerTwo(playerTwoPieces,board):
    """This populates the playerTwoPieces (white) empty set with the player two's pieces. It also adds those pieces to the board

    :param playerTwoPieces: An empty set representing player two's pieces
    :type playerTwoePieces: set
    :param board: A 2d list consisting of an 8 by 8 None objects and any prepopulated pieces
    :type board: [list]
    """
    color="WHITE"
    group=playerTwoPieces
    playerTwoPieces.update({Pawn(board,color,group,7,'A'),Pawn(board,color,group,7,'B'),Pawn(board,color,group,7,'C'),Pawn(board,color,group,7,'D'),Pawn(board,color,group,7,'E'),Pawn(board,color,group,7,'F'),Pawn(board,color,group,7,'G'),Pawn(board,color,group,7,'H')})
    #Add rank 1 pieces
    playerTwoPieces.update({Rook(board,color,group,8,'A'),Knight(board,color,group,8,'B'),Bishop(board,color,group,8,'C'),Queen(board,color,group,8,'D'),King(board,color,group,8,'E'),Bishop(board,color,group,8,'F'),Knight(board,color,group,8,'G'),Rook(board,color,group,8,'H')})

def initGame(playerOnePieces,playerTwoPieces,board):
    """Given a set reprenting player one's peices, a set w/ player two peices, and a 8 by 8 2d list filled with Nones, this mehtod would autopopulated the sets
    and lists to reflect the start of the game

    :param playerOnePieces: An empty set representing player one's pieces
    :type playerOnePieces: set
    :param playerTwoPieces: An empty set representing player two's pieces
    :type playerTwoePieces: set
    :param board: A 2d list consisting of an 8 by 8 None objects and any prepopulated pieces
    :type board: [list]
    """
    initPlayerOne(playerOnePieces,board)
    initPlayerTwo(playerTwoPieces,board)
def printBoard(board):
    """Given a 2d list representing the board w/ pieces. This function prints to terminal in a user friendly way

    :param board: A 2d list representing the board w/ pieces
    :type board: [list]
    """
    count=1
    for row in board:
        print(f'{count}-{row}')
        count+=1
    temp=[chr(ord('A')+i) for i in range(8)]
    print(temp)

def startGame():
    """This function when run on terminal would allow the user to play chess via terminal.
    """
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    initGame(playerOnePieces,playerTwoPieces,board)
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}

    while True:
        printBoard(board)
        print("Player One Put your move ex) 1A to 3B is how you move something")
        x=input().split()
        moveOne=x[0]
        moveTwo=x[2]
        board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])

if __name__ == "__main__":
    # execute only if run as a script
    startGame()