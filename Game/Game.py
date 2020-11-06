from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from  Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook
class Game():
    def __init__(self):
        self.playerOnePieces=set()
        self.playerTwoPieces=set()
        self.board=[[None]*8 for i in range(8)]
        self.initGame()
        self.possibleRow={i:i-1 for i in range(1,9)}
        self.possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}

    def initPlayerOne(self,):
        """This populates the playerOnePieces (black) empty set with the player one's pieces. It also adds those pieces to the board
        """    
        #add pawns
        #(self,self.board,color,group,row,col)
        color="BLACK"
        group=self.playerOnePieces
        self.playerOnePieces.update({Pawn(self.board,color,group,2,'A'),Pawn(self.board,color,group,2,'B'),Pawn(self.board,color,group,2,'C'),Pawn(self.board,color,group,2,'D'),Pawn(self.board,color,group,2,'E'),Pawn(self.board,color,group,2,'F'),Pawn(self.board,color,group,2,'G'),Pawn(self.board,color,group,2,'H')})

        #Add rank 1 pieces
        self.playerOnePieces.update({Rook(self.board,color,group,1,'A'),Knight(self.board,color,group,1,'B'),Bishop(self.board,color,group,1,'C'),Queen(self.board,color,group,1,'D'),King(self.board,color,group,1,'E'),Bishop(self.board,color,group,1,'F'),Knight(self.board,color,group,1,'G'),Rook(self.board,color,group,1,'H')})
        
    def initPlayerTwo(self):
        """This populates the playerTwoPieces (white) empty set with the player two's pieces. It also adds those pieces to the board
        """
        color="WHITE"
        group=self.playerTwoPieces
        self.playerTwoPieces.update({Pawn(self.board,color,group,7,'A'),Pawn(self.board,color,group,7,'B'),Pawn(self.board,color,group,7,'C'),Pawn(self.board,color,group,7,'D'),Pawn(self.board,color,group,7,'E'),Pawn(self.board,color,group,7,'F'),Pawn(self.board,color,group,7,'G'),Pawn(self.board,color,group,7,'H')})
        #Add rank 1 pieces
        self.playerTwoPieces.update({Rook(self.board,color,group,8,'A'),Knight(self.board,color,group,8,'B'),Bishop(self.board,color,group,8,'C'),Queen(self.board,color,group,8,'D'),King(self.board,color,group,8,'E'),Bishop(self.board,color,group,8,'F'),Knight(self.board,color,group,8,'G'),Rook(self.board,color,group,8,'H')})

    def initGame(self):
        """Given a set reprenting player one's peices, a set w/ player two peices, and a 8 by 8 2d list filled with Nones, this mehtod would autopopulated the sets
        and lists to reflect the start of the game. All of these inputs are already prebuilt in the start w/ the __init__ method.
        """
        self.initPlayerOne()
        self.initPlayerTwo()
    def __repr__(self):
        """Given a 2d list representing the self.board w/ pieces. This function returns a user friendly string depicting the board. The board is already provided because it is a member variable.
        """
        count=1
        for row in self.board:
            print(f'{count}-{row}')
            count+=1
        temp=[chr(ord('A')+i) for i in range(8)]
        return temp

    def startGame(self):
        """This function when run on terminal would allow the user to play chess via terminal.
        """

        while True:
            print(self.__repr__())
            print("Player One Put your move ex) 1A to 3B is how you move something")
            x=input().split()
            moveOne=x[0]
            moveTwo=x[2]
            self.board[self.possibleRow[int(moveOne[0])]][self.possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
