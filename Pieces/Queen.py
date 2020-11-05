from .piece import Piece

class Queen(Piece):
    def __init__(self,board,color,group,row,col):
        """This is an init for a queen piece. It creates the piece

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
        super().__init__(board,color,group,"Queen",row,col)

    def diagonalMoves(self):
        """Returns the possible diagonal moves the queen can make

        :return: A set of the available diagonal moves the queen can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        #Copy and paste the move set of the bishop aka diagonal
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

    def crossMoves(self):
        """Returns the possible cross moves the queen can make

        :return: A set of the available cross moves the queen can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        #Returns the set of cross moves, aka just the rook moves
        moves=set()
        #Up
        tempRow=self.row
        tempCol=self.possibleCol[self.col]
        for i in range(tempRow,8):
            if self.board[i][tempCol] is not None:
                if self.validMove(i,tempCol):
                    moves.add((i,tempCol))
                break
            else:
                moves.add((i,tempCol))
        #Down
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]
        for i in range(tempRow,-1,-1):
            if self.board[i][tempCol] is not None:
                if self.validMove(i,tempCol):
                    moves.add((i,tempCol))
                break
            else:
                moves.add((i,tempCol))
        #Left
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]-1
        for i in range(tempCol,-1,-1):
            if self.board[tempRow][i] is not None:
                if self.validMove(tempRow,i):
                    moves.add((tempRow,i))
                break
            else:
                moves.add((tempRow,i))
        #Right
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]+1
        for i in range(tempCol,8):
            if self.board[tempRow][i] is not None:
                if self.validMove(tempRow,i):
                    moves.add((tempRow,i))
                break
            else:
                moves.add((tempRow,i))
        return moves

    def availableMoves(self):
        """Returns a set of the avaiable moves the queen can make

        :return: A set of the available moves the queen can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        #Returns a set of the avaiable moves the Queen can make
        #The Queen moves basically in the directions of the rook & bishop. So I basically choose to copy & paste
        return self.diagonalMoves() | self.crossMoves()
        
        
