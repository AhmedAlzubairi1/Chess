from Game.Game import Game


def test_King_Castle():
    """Tests if you can do king side castle
    """
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king = myGame.board[0][4]
    rook = myGame.board[0][7]
    move(myGame, "2E", "4E")
    move(myGame, "1F", "2E")
    move(myGame, "1G", "3H")
    myGame.attemptKingCastle(myGame.playerOneTurn)
    assert king == myGame.board[0][6]
    assert rook == myGame.board[0][5]


def test_White_King_Castle():
    """ Tests if White pieces can do king side castle
    """
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king = myGame.board[7][4]
    rook = myGame.board[7][7]
    move(myGame, "7E", "5E")
    move(myGame, "8F", "7E")
    move(myGame, "8G", "6H")
    myGame.attemptKingCastle(not myGame.playerOneTurn)
    assert king == myGame.board[7][6]
    assert rook == myGame.board[7][5]


def test_Queen_Castle():
    """Tests Queen Side Castle
    """
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king = myGame.board[0][4]
    rook = myGame.board[0][0]
    move(myGame, "2D", "4D")
    move(myGame, "1D", "3D")
    move(myGame, "1C", "3E")
    move(myGame, "1B", "3A")
    myGame.attemptQueenCastle(myGame.playerOneTurn)
    assert king == myGame.board[0][2]
    assert rook == myGame.board[0][3]


def test_White_Queen_Castle():
    """Tests if White pieces can do Queen side castle
    """
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    king = myGame.board[7][4]
    rook = myGame.board[7][0]
    move(myGame, "7D", "5D")
    move(myGame, "8D", "6D")
    move(myGame, "8C", "7D")
    move(myGame, "8B", "6A")
    myGame.attemptQueenCastle(not myGame.playerOneTurn)
    assert king == myGame.board[7][2]
    assert rook == myGame.board[7][3]


def test_Pawn_Passant():
    """Tests if pawns can do a pawn passant capture
    """
    myGame = Game()

    def move(x, moveOne, moveTwo):
        x.board[x.possibleRow[int(moveOne[0])]][x.possibleCol[moveOne[1]]].move(int(moveTwo[0]), moveTwo[1])
    pawn = myGame.board[1][0]
    move(myGame, "2A", "4A")
    move(myGame, "4A", "5A")
    move(myGame, "7B", "5B")
    move(myGame, "5A", "6B")
    assert pawn == myGame.board[5][1]
