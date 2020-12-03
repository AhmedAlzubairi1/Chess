try:
    from Pieces.Bishop import Bishop
    from Pieces.King import King
    from Pieces.Knight import Knight
    from Pieces.Pawn import Pawn
    from Pieces.Queen import Queen
    from Pieces.Rook import Rook
except Exception:
    from .Pieces.Bishop import Bishop
    from .Pieces.King import King
    from .Pieces.Knight import Knight
    from .Pieces.Pawn import Pawn
    from .Pieces.Queen import Queen
    from .Pieces.Rook import Rook


class Game():
    def __init__(self):
        self.playerOnePieces = set()
        self.playerTwoPieces = set()
        self.board = [[None] * 8 for i in range(8)]
        # 3d board for all possible captures
        self.checkBoard = [
            [[0 for k in range(0)] for j in range(8)] for i in range(8)]
        self.initGame()
        self.possibleRow = {i: i - 1 for i in range(1, 9)}
        self.possibleCol = {chr(i): i - ord('A')
                            for i in range(ord('A'), ord('A') + 8)}
        self.turn = [1]
        self.playerOnePassantPawns = set()
        self.playerTwoPassantPawns = set()
        self.playerOneTurn = True
        # these 5 are added from check
        # Should be iether 1 or 2 to denote who won
        self.gameEnd = 0

    def resetCheckBoard(self):
        """This resets the checkBoard by making all the positions None
        """
        for i in range(len(self.checkBoard)):
            for k in range(len(self.checkBoard[i])):
                self.checkBoard[i][k] = []

    def updateCheckBoard(self, playerOne):
        """ This updated the checkBoard with PlayerTwo checks on PlayerOne if the
            playerOne paramter is true, and opposite if false
        :param playerOne: Boolean representing if it is playerOne's check
        :type playerOne: bool
        """

        # This should update with moves of playerOne
        self.resetCheckBoard()
        playerPieces = self.playerTwoPieces if playerOne \
            else self.playerOnePieces
        for piece in playerPieces:
            for capture in piece.possibleCapturesCheck():
                c, r = capture
                self.checkBoard[c][r].append(piece)

    def isCheckMate(self, playerOne):
        # Check if player is checkmated
        if playerOne:
            kingRow = self.playerOneKing.possibleCol[self.playerOneKing.col]
            kingCol = self.playerOneKing.row - 1
            status = True
            # Check if king cant make a move, but still also cant be captured
            if len(
                    self.playerOneKing.availableMoves()) == 0 and len(
                    self.checkBoard[kingCol][kingRow]) == 0:
                return False
            # Now check if the king can still move, if it can, player isnt on
            # checkmate
            for c, r in self.playerOneKing.availableMoves():
                if len(self.checkBoard[c][r]) == 0:
                    status = False
            return status
        else:
            kingRow = self.playerTwoKing.possibleCol[self.playerTwoKing.col]
            kingCol = self.playerTwoKing.row - 1
            # Example for col,row is E,8 OR 4, 7
            status = True
            # Check if king cant make a move, but still also cant be captured
            if len(
                    self.playerTwoKing.availableMoves()) == 0 and len(
                    self.checkBoard[kingCol][kingRow]) == 0:
                return False
            # Now check if the king can still move, if it can, player isnt on
            for c, r in self.playerTwoKing.availableMoves():
                if len(self.checkBoard[c][r]) == 0:
                    status = False
            return status

    def isCheck(self, playerOne):
        # Check if player is checked
        kingCol, kingRow = 0, 0
        if playerOne:
            kingRow = self.playerOneKing.possibleCol[self.playerOneKing.col]
            kingCol = self.playerOneKing.row - 1
        else:
            kingRow = self.playerTwoKing.possibleCol[self.playerTwoKing.col]
            kingCol = self.playerTwoKing.row - 1

        if len(self.checkBoard[kingCol][kingRow]) != 0:
            return True
        else:
            return False

    def initPlayerOne(self,):
        """This populates the playerOnePieces (black) empty set with the player one's
            pieces.It also adds those pieces to the board
        """
        color = "BLACK"
        group = self.playerOnePieces
        self.playerOneKing = King(self.board, color, group, 1, 'E', self)
        self.playerOnePieces.update(
            {
                Pawn(
                    self.board, color, group, 2, 'A', self), Pawn(
                    self.board, color, group, 2, 'B', self), Pawn(
                    self.board, color, group, 2, 'C', self), Pawn(
                        self.board, color, group, 2, 'D', self), Pawn(
                            self.board, color, group, 2, 'E', self), Pawn(
                                self.board, color, group, 2, 'F', self), Pawn(
                                    self.board, color, group, 2, 'G', self), Pawn(
                                        self.board, color, group, 2, 'H', self)})
        # Add rank 1 pieces
        self.playerOnePieces.update(
            {
                Rook(
                    self.board, color, group, 1, 'A', self), Knight(
                    self.board, color, group, 1, 'B', self), Bishop(
                    self.board, color, group, 1, 'C', self), Queen(
                        self.board, color, group, 1, 'D', self), self.playerOneKing, Bishop(
                            self.board, color, group, 1, 'F', self), Knight(
                                self.board, color, group, 1, 'G', self), Rook(
                                    self.board, color, group, 1, 'H', self)})

    def initPlayerTwo(self):
        """This populates the playerTwoPieces (white) empty set with the player two's pieces.
            It also adds those pieces to the board
        """
        color = "WHITE"
        group = self.playerTwoPieces
        self.playerTwoKing = King(self.board, color, group, 8, 'E', self)
        self.playerTwoPieces.update(
            {
                Pawn(
                    self.board, color, group, 7, 'A', self), Pawn(
                    self.board, color, group, 7, 'B', self), Pawn(
                    self.board, color, group, 7, 'C', self), Pawn(
                        self.board, color, group, 7, 'D', self), Pawn(
                            self.board, color, group, 7, 'E', self), Pawn(
                                self.board, color, group, 7, 'F', self), Pawn(
                                    self.board, color, group, 7, 'G', self), Pawn(
                                        self.board, color, group, 7, 'H', self)})
        # Add rank 1 pieces
        self.playerTwoPieces.update(
            {
                Rook(
                    self.board, color, group, 8, 'A', self), Knight(
                    self.board, color, group, 8, 'B', self), Bishop(
                    self.board, color, group, 8, 'C', self), Queen(
                        self.board, color, group, 8, 'D', self), self.playerTwoKing, Bishop(
                            self.board, color, group, 8, 'F', self), Knight(
                                self.board, color, group, 8, 'G', self), Rook(
                                    self.board, color, group, 8, 'H', self)})

    def initGame(self):
        """ Given a set reprenting player one's peices, a set w/ player two peices, and a 8 by 8 2d list filled with Nones,
            this mehtod would autopopulated the sets and lists to reflect the start of the game. All of these inputs
            are already prebuilt in the start w/ the __init__ method.
        """
        self.initPlayerOne()
        self.initPlayerTwo()

    def __repr__(self):
        """ Given a 2d list representing the self.board w/ pieces. This function returns a user friendly string depicting the
            board. The board is already provided because it is a member variable.
        """
        tempBoard = [[k for k in i] for i in self.board]
        # Add column labeling
        columnLetters = [chr(ord('A') + i) for i in range(8)]
        columnLetters.insert(0, '_')
        tempBoard.insert(0, columnLetters)

        # add row labeling
        count = 1
        for i in range(1, len(tempBoard)):
            tempBoard[i].insert(0, count)
            count += 1
        # Format board display
        # COde found @
        # https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
        s = [[str(e) for e in row] for row in tempBoard]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def attemptKingCastle(self, playerOne):
        """ This method is called if player wants to do a king side castle

        :param playerOne: Boolean representing if it is playerOne's attempt
        :type playerOne: bool
        :raises Exception: raises Exception if you can't do a castle
        """
        if playerOne:
            # This means black
            if self.playerOneKing.hasMoved:
                raise Exception("Can't Do castle anymore, King has moved")
            else:
                if self.board[0][5] is None and self.board[0][6] is None and self.board[0][
                        7] is not None and self.board[0][7].name == 'Rook' and self.board[0][7].color == 'BLACK':
                    # this means I can do castle
                    self.board[0][6] = self.playerOneKing
                    self.board[self.playerOneKing.row -
                               1][self.possibleCol[self.playerOneKing.col]] = None
                    self.playerOneKing.row = 1
                    self.playerOneKing.col = 'G'
                    self.board[0][7].row = 1
                    self.board[0][7].col = 'F'
                    self.board[0][5] = self.board[0][7]
                    self.board[0][7] = None

                else:
                    raise Exception(
                        "Can't do castle, spaces for king move are occupied or you are missing a rook")
        else:
            # This means playe is white
            if self.playerTwoKing.hasMoved:
                raise Exception("Can't Do castle anymore, King has moved")
            else:
                if self.board[7][5] is None and self.board[7][6] is None and self.board[7][
                        7] is not None and self.board[7][7].name == 'Rook' and self.board[7][7].color == 'WHITE':
                    # this means I can do castle
                    self.board[7][6] = self.playerTwoKing
                    self.board[self.playerTwoKing.row -
                               1][self.possibleCol[self.playerTwoKing.col]] = None
                    self.playerTwoKing.row = 8
                    self.playerTwoKing.col = 'G'
                    self.board[7][7].row = 8
                    self.board[7][7].col = 'F'
                    self.board[7][5] = self.board[7][7]
                    self.board[7][7] = None

                else:
                    raise Exception(
                        "Can't do castle, spaces for king move are occupied or you are missing a rook")

    def attemptQueenCastle(self, playerOne):
        """ This method is called if player wants to do a queen side castle

        :param playerOne: Boolean representing if it is playerOne's attempt
        :type playerOne: bool
        :raises Exception: raises Exception if you can't do a castle
        """
        if playerOne:
            # This means black
            if self.playerOneKing.hasMoved:
                raise Exception("Can't Do castle anymore, King has moved")
            else:
                if self.board[0][1] is None and self.board[0][2] is None and self.board[0][3] is None and self.board[
                        0][0] is not None and self.board[0][0].name == 'Rook' and self.board[0][0].color == 'BLACK':
                    # this means I can do castle
                    self.board[0][2] = self.playerOneKing
                    self.board[self.playerOneKing.row -
                               1][self.possibleCol[self.playerOneKing.col]] = None
                    self.playerOneKing.row = 1
                    self.playerOneKing.col = 'C'
                    self.board[0][0].row = 1
                    self.board[0][0].col = 'D'
                    self.board[0][3] = self.board[0][0]
                    self.board[0][0] = None

                else:
                    raise Exception(
                        "Can't do castle, spaces for king move are occupied or you are missing a rook")
        else:
            # This means playe is white
            if self.playerTwoKing.hasMoved:
                raise Exception("Can't Do castle anymore, King has moved")
            else:
                if self.board[7][1] is None and self.board[7][2] is None and self.board[7][3] is None and self.board[
                        7][0] is not None and self.board[7][0].name == 'Rook' and self.board[7][0].color == 'WHITE':
                    # this means I can do castle
                    self.board[7][2] = self.playerTwoKing
                    self.board[self.playerTwoKing.row -
                               1][self.possibleCol[self.playerTwoKing.col]] = None
                    self.playerTwoKing.row = 8
                    self.playerTwoKing.col = 'C'
                    self.board[7][0].row = 8
                    self.board[7][0].col = 'D'
                    self.board[7][3] = self.board[7][0]
                    self.board[7][0] = None

                else:
                    raise Exception(
                        "Can't do castle, spaces for king move are occupied or you are missing a rook")

    def startGame(self):
        """This function when run on terminal would allow the user to play chess via terminal.
        """
        print("Player One Put your move ex) 1A to 3B is how you move something")
        print("If you want to castle type 'king-side castle' or 'queen-side castle'" +
              "for the direction of castle you want")

        while True:
            # Update the capture board to see the captures
            self.updateCheckBoard(self.playerOneTurn)
            # print(self.pBoard())
            if self.isCheckMate(self.playerOneTurn):
                print(self.__repr__())
                if self.playerOneTurn:
                    print('Player One lost, checkmate')
                else:
                    print('Player two lost, checkmate')
                break
            if self.playerOneTurn:
                print(
                    f'Player One turn \n Note: player TWO passant are {self.playerTwoPassantPawns}')
                self.playerOnePassantPawns = set()
            else:
                print(
                    f' Player two Turn \n Note: player one passant are {self.playerOnePassantPawns}')
                self.playerTwoPassantPawns = set()

            if self.isCheck(self.playerOneTurn):
                if self.playerOneTurn:
                    print('Player One in check')
                else:
                    print('Player two in check')

            print(self.__repr__())
            x = input().split()
            moveOne = x[0]
            moveTwo = x[1] if moveOne.lower(
            ) == 'king-side' or moveOne.lower() == 'queen-side' else x[2]
            try:
                if moveOne.lower() == 'king-side':
                    self.attemptKingCastle(self.playerOneTurn)
                elif moveOne.lower() == 'queen-side':
                    self.attemptQueenCastle(self.playerOneTurn)
                elif self.isCheck(self.playerOneTurn):
                    print('Make a move to move away from Check')
                    self.board[self.possibleRow[int(moveOne[0])]][self.possibleCol[moveOne[1]]].move(
                        int(moveTwo[0]), moveTwo[1])
                else:
                    self.board[self.possibleRow[int(moveOne[0])]][self.possibleCol[moveOne[1]]].move(
                        int(moveTwo[0]), moveTwo[1])
                self.playerOneTurn = not self.playerOneTurn
                print('\n' * 4)
            except Exception as identifier:
                print(identifier)

    def pBoard(self):
        """ Given a 2d list representing the self.board w/ pieces. This function returns a user friendly string
            depicting the board. The board is already provided because it is a member variable.
        """
        tempBoard = [[k for k in i] for i in self.checkBoard]
        # Add column labeling
        columnLetters = [chr(ord('A') + i) for i in range(8)]
        columnLetters.insert(0, '_')
        tempBoard.insert(0, columnLetters)

        # add row labeling
        count = 1
        for i in range(1, len(tempBoard)):
            tempBoard[i].insert(0, count)
            count += 1
        # Format board display
        # COde found @
        # https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
        s = [[str(e) for e in row] for row in tempBoard]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)
