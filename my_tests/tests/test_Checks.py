from Game.Game import Game


def test_Check():
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    move(myGame, "7E", "5E")
    move(myGame, "5E", "4E")
    move(myGame, "4E", "3E")
    move(myGame, "2D", "4D")
    move(myGame, "1D", "3D")
    move(myGame, "8E", "7E")
    move(myGame, "3D", "3E")
    myGame.updateCheckBoard(False)
    assert myGame.isCheck(False)
    myGame.updateCheckBoard(True)
    assert myGame.isCheck(True) == False



def test_CheckMate():
    myGame = Game()
    print(myGame)
    print(myGame.pBoard())

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    move(myGame,"2H","4H")
    move(myGame,"4H","5H")
    move(myGame,"5H","6H")
    move(myGame,"1H","4H")
    move(myGame,"4H","4G")
    move(myGame,"4G","4H")
    move(myGame, "2C", "4C")
    move(myGame, "1D", "2C")
    move(myGame, "2C", "4E")
    move(myGame, "7E", "5E")
    move(myGame, "4E", "5E")
    move(myGame, "2D", "3D")
    move(myGame, "1C", "4F")
    move(myGame, "4F", "5G")
    myGame.updateCheckBoard(False)
    assert myGame.isCheckMate(False)
    myGame.updateCheckBoard(True)
    assert myGame.isCheckMate(True) == False
