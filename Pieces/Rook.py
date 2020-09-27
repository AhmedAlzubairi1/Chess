'''
This is a class to represent the Rook
'''
from Piece import Piece

class Rook(Piece):
    def __init__(self,board,group,row,col):
        super().__init__(board,group,"Rook",row,col)
        print(self.row)

    def availableMoves(self):
        #Returns a set of the avaiable moves the Rook can make
        moves=set()
        #Up
        tempRow=self.row
        tempCol=self.possibleCol[self.col]
        for i in range(tempRow,8):
            if self.board[i][tempCol] is not None:
                if self.checkIfNotNearKing(i,tempCol):
                    moves.add((i,tempCol))
                break
            else:
                if self.checkIfNotNearKing(i,tempCol):
                    moves.add((i,tempCol))
        #Down
        tempRow=self.row-2
        tempCol=self.possibleCol[self.col]
        for i in range(tempRow,-1,-1):
            if self.board[i][tempCol] is not None:
                if self.checkIfNotNearKing(i,tempCol):
                    moves.add((i,tempCol))
                break
            else:
                if self.checkIfNotNearKing(i,tempCol):
                    moves.add((i,tempCol))
        #Left
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]-1
        for i in range(tempCol,-1,-1):
            if self.board[tempRow][i] is not None:
                if self.checkIfNotNearKing(tempRow,i):
                    moves.add((tempRow,i))
                break
            else:
                if self.checkIfNotNearKing(tempRow,i):
                    moves.add((tempRow,i))
        #Right
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]+1
        for i in range(tempCol,8):
            if self.board[tempRow][i] is not None:
                if self.checkIfNotNearKing(tempRow,i):
                    moves.add((tempRow,i))
                break
            else:
                if self.checkIfNotNearKing(tempRow,i):
                    moves.add((tempRow,i))
        return moves