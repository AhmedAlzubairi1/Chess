from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from  Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from prettytable import PrettyTable

class Game():
    def __init__(self):
        self.playerOnePieces=set()
        self.playerTwoPieces=set()
        self.board=[[None]*8 for i in range(8)]
        self.initGame()
        self.possibleRow={i:i-1 for i in range(1,9)}
        self.possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
        self.turn=[1]
        self.playerOnePassantPawns=set()
        self.playerTwoPassantPawns=set()
        self.playerOneTurn=True
    def initPlayerOne(self,):
        """This populates the playerOnePieces (black) empty set with the player one's pieces. It also adds those pieces to the board
        """    
        #add pawns
        #(self,self.board,color,group,row,col)
        color="BLACK"
        group=self.playerOnePieces
        self.playerOnePieces.update({Pawn(self.board,color,group,2,'A',self),Pawn(self.board,color,group,2,'B',self),Pawn(self.board,color,group,2,'C',self),Pawn(self.board,color,group,2,'D',self),Pawn(self.board,color,group,2,'E',self),Pawn(self.board,color,group,2,'F',self),Pawn(self.board,color,group,2,'G',self),Pawn(self.board,color,group,2,'H',self)})

        #Add rank 1 pieces
        self.playerOnePieces.update({Rook(self.board,color,group,1,'A',self),Knight(self.board,color,group,1,'B',self),Bishop(self.board,color,group,1,'C',self),Queen(self.board,color,group,1,'D',self),King(self.board,color,group,1,'E',self),Bishop(self.board,color,group,1,'F',self),Knight(self.board,color,group,1,'G',self),Rook(self.board,color,group,1,'H',self)})
        
    def initPlayerTwo(self):
        """This populates the playerTwoPieces (white) empty set with the player two's pieces. It also adds those pieces to the board
        """
        color="WHITE"
        group=self.playerTwoPieces
        self.playerTwoPieces.update({Pawn(self.board,color,group,7,'A',self),Pawn(self.board,color,group,7,'B',self),Pawn(self.board,color,group,7,'C',self),Pawn(self.board,color,group,7,'D',self),Pawn(self.board,color,group,7,'E',self),Pawn(self.board,color,group,7,'F',self),Pawn(self.board,color,group,7,'G',self),Pawn(self.board,color,group,7,'H',self)})
        #Add rank 1 pieces
        self.playerTwoPieces.update({Rook(self.board,color,group,8,'A',self),Knight(self.board,color,group,8,'B',self),Bishop(self.board,color,group,8,'C',self),Queen(self.board,color,group,8,'D',self),King(self.board,color,group,8,'E',self),Bishop(self.board,color,group,8,'F',self),Knight(self.board,color,group,8,'G',self),Rook(self.board,color,group,8,'H',self)})

    def initGame(self):
        """Given a set reprenting player one's peices, a set w/ player two peices, and a 8 by 8 2d list filled with Nones, this mehtod would autopopulated the sets
        and lists to reflect the start of the game. All of these inputs are already prebuilt in the start w/ the __init__ method.
        """
        self.initPlayerOne()
        self.initPlayerTwo()
    def __repr__(self):
        """Given a 2d list representing the self.board w/ pieces. This function returns a user friendly string depicting the board. The board is already provided because it is a member variable.
        """
        '''
        count=1
        for row in self.board:
            print(f'{count}-{row}')
            count+=1
        temp=[chr(ord('A')+i) for i in range(8)]
        return temp
        '''

        tempBoard=[[k for k in i] for i in self.board]        
        #Add column labeling
        columnLetters = [chr(ord('A')+i)       for i in range(8)]
        columnLetters.insert(0,'_')
        tempBoard.insert(0,columnLetters)
        
        #add row labeling
        count=1
        for i in range(1,len(tempBoard)):
            tempBoard[i].insert(0,count)
            count+=1
        #Format board display
        # COde found @ https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
        s = [[str(e) for e in row] for row in tempBoard]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def startGame(self):
        """This function when run on terminal would allow the user to play chess via terminal.
        """

        while True:
            # I am reseting the passant set because the opposing player can only take the passant piece on the first move it is possible to capture it only
            if self.playerOneTurn:
                print(f' player TWO passant are {self.playerTwoPassantPawns}')
                self.playerOnePassantPawns=set()
            else:
                print(f' player one passant are {self.playerOnePassantPawns}')
                self.playerTwoPassantPawns=set()
            print(self.__repr__())
            print("Player One Put your move ex) 1A to 3B is how you move something")
            x=input().split()
            moveOne=x[0]
            moveTwo=x[2]
            self.board[self.possibleRow[int(moveOne[0])]][self.possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
            self.playerOneTurn= not self.playerOneTurn
            print('\n'*4)

