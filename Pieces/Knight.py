from .piece import Piece

class Knight(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"Knight",row,col)

    def availableMoves(self):
        #Returns a set of the avaiable moves the Knight can make
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


