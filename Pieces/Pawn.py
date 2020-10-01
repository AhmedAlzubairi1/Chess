from Piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"Pawn",row,col)

    def availableMoves(self):
        #Returns a set of the avaiable moves the Pawn can make
        moves=set()
        #Up
        # ex row=2 col=C
        tempRow=self.row-1 #1
        tempCol=self.possibleCol[self.col] #2
        #top position
        if  0<=tempRow+1<=7 and self.board[tempRow+1][tempCol] is None:
            moves.add((tempRow+1,tempCol))

        #if at second col
        if tempRow==1 and self.board[tempRow+1][tempCol] is None and self.board[tempRow+2][tempCol] is None:
            moves.add((tempRow+2,tempCol))

        #Now the capture moves
        if 0<=tempRow+1<=7 and 0<=tempCol-1<=7 and self.validMove(tempRow,tempCol):
            moves.add((tempRow+1,tempCol-1))
        if 0<=tempRow+1<=7 and 0<=tempCol+1<=7 and self.validMove(tempRow,tempCol):
            moves.add((tempRow+1,tempCol+1))

        return moves
