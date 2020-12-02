from .piece import Piece

class Bishop(Piece):
    def __init__(self,board,color,group,row,col,game):
        """This is an init for a bishop piece. It creates the piece

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
        super().__init__(board,color,group,"Bishop",row,col,game)

    def availableMoves(self):
        """Returns a set of the avaiable moves the Bishop can make

        :return: A set of the available moves the bishop can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        #Returns a set of the avaiable moves the Bishop can make
        moves=set()
        tempRow=self.row
        tempCol=self.possibleCol[self.col]-1
        #Top left diagonal 
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMove(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow+=1
            tempCol-=1

        #Top right diagonal 
        tempRow=self.row
        tempCol=self.possibleCol[self.col]+1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMove(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow+=1
            tempCol+=1

        #Bottom left diagonal 
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]-1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMove(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow-=1
            tempCol-=1

        #Bottom right diagonal 
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]+1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMove(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow-=1
            tempCol+=1
        return moves
    def possibleCapturesCheck(self):
        """Returns a set of the avaiable moves the bishop can make for a king check

        :return: A set of the available moves the bishop can make for check. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        moves=set()
        tempRow=self.row
        tempCol=self.possibleCol[self.col]-1
        #Top left diagonal 
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMoveIncludingKing(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow+=1
            tempCol-=1

        #Top right diagonal 
        tempRow=self.row
        tempCol=self.possibleCol[self.col]+1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMoveIncludingKing(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow+=1
            tempCol+=1

        #Bottom left diagonal 
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]-1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMoveIncludingKing(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow-=1
            tempCol-=1

        #Bottom right diagonal 
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]+1
        while 0<=tempCol<=7 and 0<=tempRow<=7:
            if self.board[tempRow][tempCol] is None:
                moves.add((tempRow,tempCol))
            else:
                if self.validMoveIncludingKing(tempRow,tempCol):
                    moves.add((tempRow,tempCol))
                break
            tempRow-=1
            tempCol+=1
        return moves