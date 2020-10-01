

# some_file.py
# insert at 1, 0 is the script path (or '' in REPL)
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook

def initPlayerOne(playerOnePieces,board):
    #add pawns
    #(self,board,color,group,row,col)
    color="BLACK"
    group=playerOnePieces
    playerOnePieces.update({Pawn(board,color,group,2,'A'),Pawn(board,color,group,2,'B'),Pawn(board,color,group,2,'C'),Pawn(board,color,group,2,'D'),Pawn(board,color,group,2,'E'),Pawn(board,color,group,2,'F'),Pawn(board,color,group,2,'G'),Pawn(board,color,group,2,'H')})
    #Add rank 1 pieces
    playerOnePieces.update({Rook(board,color,group,1,'A'),Knight(board,color,group,1,'B'),Bishop(board,color,group,1,'C'),Queen(board,color,group,1,'D'),King(board,color,group,1,'E'),Bishop(board,color,group,1,'F'),Knight(board,color,group,1,'G'),Rook(board,color,group,1,'H')})
    
def initPlayerTwo(playerTwoPieces,board):
    color="WHITE"
    group=playerTwoPieces
    playerTwoPieces.update({Pawn(board,color,group,2,'A'),Pawn(board,color,group,2,'B'),Pawn(board,color,group,2,'C'),Pawn(board,color,group,2,'D'),Pawn(board,color,group,2,'E'),Pawn(board,color,group,2,'F'),Pawn(board,color,group,2,'G'),Pawn(board,color,group,2,'H')})
    #Add rank 1 pieces
    playerTwoPieces.update({Rook(board,color,group,1,'A'),Knight(board,color,group,1,'B'),Bishop(board,color,group,1,'C'),Queen(board,color,group,1,'D'),King(board,color,group,1,'E'),Bishop(board,color,group,1,'F'),Knight(board,color,group,1,'G'),Rook(board,color,group,1,'H')})

def initGame(playerOnePieces,playerTwoPieces,board):
    initPlayerOne(playerOnePieces,board)
    initPlayerTwo(playerTwoPieces,board)

if __name__ == "__main__":
    # execute only if run as a script
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*7 for i in range(8)]
    #initGame(playerOnePieces,playerTwoPieces,board)
    print(board)    