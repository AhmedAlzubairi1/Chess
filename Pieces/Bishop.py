from Piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"Bishop",row,col)
        print(self.row)

    def availableMoves(self):
        #Returns a set of the avaiable moves the Bishop can make
        moves=set()
        #
        return moves
