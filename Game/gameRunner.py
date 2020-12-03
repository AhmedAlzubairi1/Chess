from Game import Game
x = Game()
#x.startGame()
#Testing king passant
myGame = Game()
def move(x,moveOne,moveTwo):
    x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])

move(myGame,"2H","4H")

move(myGame,"4H","5H")

move(myGame,"5H","6H")

move(myGame,"1H","4H")

move(myGame,"4H","4G")

move(myGame,"4G","4H")

move(myGame,"2C","4C")
move(myGame,"1D","2C")
move(myGame,"2C","4E")
move(myGame,"7E","5E")
move(myGame,"4E","5E")

myGame.updateCheckBoard(False)
print(myGame.pBoard())
print(myGame)
print(myGame.isCheckMate(False))