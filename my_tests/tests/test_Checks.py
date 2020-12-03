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


def test_CheckMate():
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    move(myGame, "2C", "4C")
    move(myGame, "1D", "2C")
    move(myGame, "2C", "4E")
    move(myGame, "7E", "5E")
    move(myGame, "4E", "5E")
    myGame.updateCheckBoard(False)
    assert myGame.isCheckMate(False)
