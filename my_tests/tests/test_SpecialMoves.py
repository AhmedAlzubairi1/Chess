from Game.Pieces.Rook import Rook
from Game.Pieces.Queen import Queen
from Game.Pieces.Pawn import Pawn
from Game.Pieces.Knight import Knight
from Game.Pieces.King import King
from Game.Pieces.Bishop import Bishop
from Game.Game import Game

def test_King_Castle():
    myGame = Game()
    def move(x,moveOne,moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king=myGame.board[0][4]
    rook=myGame.board[0][7]
    move(myGame,"2E","4E")
    move(myGame,"1F","2E")
    move(myGame,"1G","3H")
    myGame.attemptKingCastle(myGame.playerOneTurn)
    assert king == myGame.board[0][6]
    assert rook == myGame.board[0][5]
def test_Queen_Castle():
    myGame = Game()
    def move(x,moveOne,moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king=myGame.board[0][4]
    rook=myGame.board[0][0]
    move(myGame,"2D","4D")
    move(myGame,"1D","3D")
    move(myGame,"1C","3E")
    move(myGame,"1B","3A")
    myGame.attemptQueenCastle(myGame.playerOneTurn)
    assert king == myGame.board[0][2]
    assert rook == myGame.board[0][3]
def test_Pawn_Passant():
    myGame = Game()
    def move(x,moveOne,moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    pawn=myGame.board[1][0]
    move(myGame,"2A","4A")
    move(myGame,"4A","5A")
    move(myGame,"7B","5B")
    move(myGame,"5A","6B")
    assert pawn == myGame.board[5][1]
