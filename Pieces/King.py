from piece import Piece

class King(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"King",row,col)

    def availableMoves(self):
        #Returns a set of the avaiable moves the King can make
        moves=set()        
        tempRow=self.row-1
        tempCol=self.possibleCol[self.col]
        direction=[(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for (i,k) in direction:
            if 0<=tempRow+i<=7 and 0<=tempCol+k<=7 and (self.board[tempRow+i][tempCol+k] is None or self.validMove(tempRow+i,tempCol+k)):
                moves.add((tempRow+i,tempCol+k))            
        return moves
