'''
This is a general class to describe the characteristics that every piece should have
'''

class Piece():
    def __init__(self,board,color,group,name,row,col,game):
        """This is an init for any piece. It creates the piece. It should be inherited by a specific piece with custom parameters.

        :param board: A 2d list representing a board state
        :type board: [list]
        :param color: A string that is either 'BLACK' or 'WHITE'
        :type color: str
        :param group: A set representing all the pieces of the player
        :type group: set
        :param name: A str representing the name of the piece. Options of the str are : {'Pawn','Rook','Knight','King','Queen','Bishop'}
        :type name: str
        :param row: a number from 1 to 8 representing the row
        :type row: row
        :param col: a letter from 'A' to 'H' representing the col of the piece
        :type col: str
        """
        possiblePieces={'Pawn','Rook','Knight','King','Queen','Bishop'}
        self.game=game
        self.possibleRow={i:i-1 for i in range(1,9)}
        self.possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
        #Check they are valid
        assert name in possiblePieces , f"Invalid pawn type. Make sure name is one of {possiblePieces}"
        assert col in self.possibleCol , f"Invalid column location, make sure it is between A and H (inclusive and uppercase)"
        assert row in self.possibleRow , f"Invalid row location, make sure it is between 1 and 8 (inclusive)"
        assert color in ("BLACK","WHITE") , f"Invalid color for piece, make it it is either BLACK or WHITE"
        self.board=board
        self.color=color
        self.group=group
        self.name=name
        self.row=row
        self.col=col
        #I add an original col & row for hash and equal purposes
        self.origRow=row
        self.origCol=col
        #Add to group and board
        self.board[self.row-1][self.possibleCol[self.col]]=self
        self.group.add(self)
        #added hasMoved variable for the en passant and castling rules
        self.hasMoved=False


    def availableMoves(self):
        """ returns the available moves of the piece
        """
        #Returns a set of the avaiable moves the piece can make
        pass
    def validMove(self,row,col):
        """Given a desired move of the piece, the method returns true if the player can move the piece to that location.

        :param row: The row of the desired location. Number between 1 to 8
        :type row: int
        :param col: The column of the desired location. Letter between A and H.
        :type col: str
        :return: True if the desired moove can be made, or false if it can't be made.
        :rtype: bool
        """
        print(f'valid move requested row,col is {(row,col)} and that color is {self.board[row][col].color} and our color is {self.color}')
        if self.board[row][col].color != self.color and self.notKing(row,col):
            return True
        return False

        

    def notKing(self,row,col):
        """ Checks if the desired location is a king or not.

        :param row: The desired row
        :type row: int
        :param col: The desired column
        :type col: str
        :return: True if the location specified is not a king piece, false if it is.
        :rtype: bool
        """
        #TODO this should check if the location is a king or near a king. If it is, return False. Else return True
        if self.board[row][col].name != 'King':
            return True
        return False
    
    def move(self,targetRow,targetCol):
        """Given a row and column, the piece moves to that location.

        :param targetRow: The target row
        :type targetRow: int
        :param targetCol: The target column
        :type targetCol: str
        :return: Returns true if the move was successfully made with no issue. False if an error occured.
        :rtype: bool
        """
        #Example input : 1A for bottom left location 
        if (targetRow-1,self.possibleCol[targetCol]) in self.availableMoves():
            #Check if there is already a piece there. If so, remove it and replace
            if self.board[targetRow-1][self.possibleCol[targetCol]] is not None:
                print("if")
                self.board[targetRow-1][self.possibleCol[targetCol]].removeFromGroup()
                self.board[targetRow-1][self.possibleCol[targetCol]]=self
                self.board[self.row-1][self.possibleCol[self.col]]=None
                self.row=targetRow
                self.col=targetCol
            else:
                print("else")
                #Else, just move it to that location
                self.board[targetRow-1][self.possibleCol[targetCol]]=self
                self.board[self.row-1][self.possibleCol[self.col]]=None
                self.row=targetRow
                self.col=targetCol
            self.hasMoved=True
            self.game.turn[0]+=1
            print(self.game.turn[0])
            
        else:
            print("error FALSE MOVE")
            print(f' requested {targetRow,targetCol} but available moves are {self.availableMoves()} ALSO {len(self.availableMoves())==0}')
            print(self.__repr__())
            return False

    def removeFromGroup(self):
        """This removes the piece from the current player's set
        """
        print('test')
        print(self.group)
        print(self)
        print(self in self.group)
        print('test')
        self.group.remove(self)
    
    def __hash__(self):
        """Returns the hash of the piece

        :return: Returns the hash of the piece
        :rtype: int
        """
        return hash((self.name,self.origRow,self.origCol))
    def __eq__(self,other):
        """Returns true if the piece is the same as another

        :param other: The other piece
        :type other: Piece
        :return: True if the piece is the same. False if it isn't
        :rtype: bool
        """
        return type(other) == type(self) and self.name == other.name and self.origCol==other.origCol and self.origRow==other.origRow
    
    def __repr__(self):
        """Returns a string representation of the piece to denote the color, the name, and location

        :return: A string to denote the color, the name, and location
        :rtype: str
        """
        return f'{self.color[0]}-{self.name}-{self.row}{self.col}' 

#Ignoe
'''
class temp(piece):
    def __init__(self,group,name,row,col):
        super().__init__(group,name,row,col)
'''