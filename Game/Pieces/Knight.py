from .piece import Piece

class Knight(Piece):
    def __init__(self,board,color,group,row,col,game):
        """This is an init for a knight piece. It creates the piece

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
        super().__init__(board,color,group,"Knight",row,col,game)

    def availableMoves(self):
        """Returns a set of the avaiable moves the knight can make

        :return: A set of the available moves the knight can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        moves=set()
        #The knight moves in 8 different moves in 8 different L like moves
        
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]
        #This is the L moves direction
        direction=[(2,-1),(2,1),(-2,-1),(-2,1), (1,-2), (-1,-2), (1,2), (-1,2)]     
        for (i,k) in direction:
            if 0<=tempRow+i<=7 and 0<=tempCol+k<=7 and (self.board[tempRow+i][tempCol+k] is None or self.validMove(tempRow+i,tempCol+k)):
                moves.add((tempRow+i,tempCol+k))            
        return moves

    def possibleCapturesCheck(self):
        """Returns a set of the avaiable moves the knight can make for a king check

        :return: A set of the available moves the knight can make for check. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        moves=set()
        #The knight moves in 8 different moves in 8 different L like moves
        
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]
        #This is the L moves direction
        direction=[(2,-1),(2,1),(-2,-1),(-2,1), (1,-2), (-1,-2), (1,2), (-1,2)]     
        for (i,k) in direction:
            if 0<=tempRow+i<=7 and 0<=tempCol+k<=7 and (self.board[tempRow+i][tempCol+k] is None or self.validMoveIncludingKing(tempRow+i,tempCol+k)):
                moves.add((tempRow+i,tempCol+k))            
        return moves
