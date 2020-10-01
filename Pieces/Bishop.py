from Piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"Bishop",row,col)

    def availableMoves(self):
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
