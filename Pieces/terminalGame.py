from King import King
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
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
    playerTwoPieces.update({Pawn(board,color,group,7,'A'),Pawn(board,color,group,7,'B'),Pawn(board,color,group,7,'C'),Pawn(board,color,group,7,'D'),Pawn(board,color,group,7,'E'),Pawn(board,color,group,7,'F'),Pawn(board,color,group,7,'G'),Pawn(board,color,group,7,'H')})
    #Add rank 1 pieces
    playerTwoPieces.update({Rook(board,color,group,8,'A'),Knight(board,color,group,8,'B'),Bishop(board,color,group,8,'C'),Queen(board,color,group,8,'D'),King(board,color,group,8,'E'),Bishop(board,color,group,8,'F'),Knight(board,color,group,8,'G'),Rook(board,color,group,8,'H')})

def initGame(playerOnePieces,playerTwoPieces,board):
    initPlayerOne(playerOnePieces,board)
    initPlayerTwo(playerTwoPieces,board)
def printBoard(board):
    count=1
    for row in board:
        print(f'{count}-{row}')
        count+=1
    temp=[chr(ord('A')+i) for i in range(8)]
    print(temp)
if __name__ == "__main__":
    # execute only if run as a script
    playerOnePieces=set()
    playerTwoPieces=set()
    board=[[None]*8 for i in range(8)]
    initGame(playerOnePieces,playerTwoPieces,board)
    possibleRow={i:i-1 for i in range(1,9)}
    possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}

    while True:
        printBoard(board)
        print("Player One Put your move ex) 1A to 3B is how you move something")
        x=input().split()
        moveOne=x[0]
        moveTwo=x[2]
        board[possibleRow[int(moveOne[0])]][possibleCol[moveOne[1]]].move(int(moveTwo[0]),moveTwo[1])
        
    