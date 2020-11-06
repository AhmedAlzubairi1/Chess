from .piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col):
        """This is an init for a pawn piece. It creates the piece

        :param board: A 2d list representing a board state
        :type board: [list]
        :param color: A string that is either 'BLACK' or 'WHITE'
        :type color: str
        :param group: A set representing all the pieces of the player
        :type group: set
        :param row: a number from 1 to 8 representing the row
        :type row: row
        :param col: a letter from 'A' to 'H' representing the col of the piece
        :type col: str
        """
        super().__init__(board,color,group,"Pawn",row,col)

    def availableMoves(self):
        """Returns a set of the avaiable moves the pawn can make

        :return: A set of the available moves the pawn can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        moves=set()
        #Up
        # ex row=2 col=C
        tempRow=self.row-1 #1
        tempCol=self.possibleCol[self.col] #2
        #if black:
        if self.color == 'BLACK':
            #top position
            if  0<=tempRow+1<=7 and self.board[tempRow+1][tempCol] is None:
                moves.add((tempRow+1,tempCol))

            #if at second col
            if tempRow==1 and self.board[tempRow+1][tempCol] is None and self.board[tempRow+2][tempCol] is None:
                moves.add((tempRow+2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow+1<=7 and 0<=tempCol-1<=7 and self.board[tempRow+1][tempCol-1] is not None and self.validMove(tempRow+1,tempCol-1):
                moves.add((tempRow+1,tempCol-1))
            if 0<=tempRow+1<=7 and 0<=tempCol+1<=7 and self.board[tempRow+1][tempCol+1] is not None and self.validMove(tempRow+1,tempCol+1):
                moves.add((tempRow+1,tempCol+1))
        else:
            #top position
            if  0<=tempRow-1<=7 and self.board[tempRow-1][tempCol] is None:
                moves.add((tempRow-1,tempCol))

            #if at second col
            if tempRow==6 and self.board[tempRow-1][tempCol] is None and self.board[tempRow-2][tempCol] is None:
                moves.add((tempRow-2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow-1<=7 and 0<=tempCol-1<=7 and self.board[tempRow-1][tempCol-1] is not None and self.validMove(tempRow-1,tempCol-1):
                moves.add((tempRow-1,tempCol-1))
            if 0<=tempRow-1<=7 and 0<=tempCol+1<=7 and self.board[tempRow-1][tempCol+1] is not None and self.validMove(tempRow-1,tempCol+1):
                moves.add((tempRow-1,tempCol+1))
        return moves
