from .piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col,game):
        """This is an init for a pawn piece. It creates the piece

        :param board: A 2d list representing a board state
        :type board: [list]
        :param color: A string that is either 'BLACK' or 'WHITE'
        :type color: str
        :param group: A set representing all the pieces of the player
        :type group: set
        :param row: a number from 1 to 8 representing the row
        :type row: row
        :param col: a letter from 'A' to 'H' representing the col of the piece
        :type col: str
        """
        super().__init__(board,color,group,"Pawn",row,col,game)

    def availableMoves(self):
        """Returns a set of the avaiable moves the pawn can make

        :return: A set of the available moves the pawn can make. It is a set of tuples of the rows and colms that the move can move to
        :rtype: {(int,str)}
        """
        moves=set()
        #Up
        # ex row=2 col=C
        tempRow=self.row-1 #1
        tempCol=self.possibleCol[self.col] #2
        #if black:
        if self.color == 'BLACK':
            #top position
            if  0<=tempRow+1<=7 and self.board[tempRow+1][tempCol] is None:
                moves.add((tempRow+1,tempCol))

            #if at second col
            if tempRow==1 and self.board[tempRow+1][tempCol] is None and self.board[tempRow+2][tempCol] is None:
                moves.add((tempRow+2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow+1<=7 and 0<=tempCol-1<=7 and self.board[tempRow+1][tempCol-1] is not None and self.validMove(tempRow+1,tempCol-1):
                moves.add((tempRow+1,tempCol-1))
            
            if 0<=tempRow+1<=7 and 0<=tempCol+1<=7 and self.board[tempRow+1][tempCol+1] is not None and self.validMove(tempRow+1,tempCol+1):
                moves.add((tempRow+1,tempCol+1))
            
            #En passant capture
            #I would need to check if that move is en passant and move up one unit
            #left capture of black
            if 0<=tempRow+1<=7 and 0<=tempCol-1<=7 and self.board[tempRow+1][tempCol-1] is None and self.board[tempRow][tempCol-1] in self.game.playerTwoPassantPawns:
                
                moves.add((tempRow+1,tempCol-1))

            if 0<=tempRow+1<=7 and 0<=tempCol+1<=7 and self.board[tempRow+1][tempCol+1] is None and self.board[tempRow][tempCol+1] in self.game.playerTwoPassantPawns:
                moves.add((tempRow+1,tempCol+1))

        else:
            #top position
            if  0<=tempRow-1<=7 and self.board[tempRow-1][tempCol] is None:
                moves.add((tempRow-1,tempCol))

            #if at second col
            if tempRow==6 and self.board[tempRow-1][tempCol] is None and self.board[tempRow-2][tempCol] is None:
                moves.add((tempRow-2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow-1<=7 and 0<=tempCol-1<=7 and self.board[tempRow-1][tempCol-1] is not None and self.validMove(tempRow-1,tempCol-1):
                moves.add((tempRow-1,tempCol-1))
            if 0<=tempRow-1<=7 and 0<=tempCol+1<=7 and self.board[tempRow-1][tempCol+1] is not None and self.validMove(tempRow-1,tempCol+1):
                moves.add((tempRow-1,tempCol+1))
            #En passant capture
            #I would need to check if that move is en passant and move up one unit
            #left capture of white
            if 0<=tempRow-1<=7 and 0<=tempCol-1<=7 and self.board[tempRow-1][tempCol-1] is None and self.board[tempRow][tempCol-1] in self.game.playerOnePassantPawns:
                moves.add((tempRow-1,tempCol-1))
            #Right en passant capture
            if 0<=tempRow-1<=7 and 0<=tempCol+1<=7 and self.board[tempRow-1][tempCol+1] is None and self.board[tempRow][tempCol+1] in self.game.playerOnePassantPawns:
                moves.add((tempRow-1,tempCol+1))
        return moves
    
    def isPassant(self,tempOriginalRow,targetRow,targetCol):
        print((self.hasMoved,self.col,targetCol,abs(tempOriginalRow-targetRow)))
        if self.hasMoved == False and self.col == targetCol and abs(tempOriginalRow-targetRow)==2:
            return True
        return False
    
    def move(self,targetRow,targetCol):
        """Given a row and column, the piece moves to that location. This is for a pawn specific move to account for en passant cases.

        :param targetRow: The target row
        :type targetRow: int
        :param targetCol: The target column
        :type targetCol: str
        :return: Returns true if the move was successfully made with no issue. False if an error occured.
        :rtype: bool
        """
        #Example input : 1A for bottom left location 
        preMoveRow=self.row
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
                #Note: I need to know check of the case it is en passant capture, not just a regular move
                self.board[targetRow-1][self.possibleCol[targetCol]]=self
                self.board[self.row-1][self.possibleCol[self.col]]=None
                self.row=targetRow
                self.col=targetCol
                #Check if you can do an en passant capture on oppoenent piece
                if self.color == 'BLACK' and self.board[targetRow-2][self.possibleCol[targetCol]] in self.game.playerTwoPassantPawns:
                    self.board[targetRow-2][self.possibleCol[targetCol]].removeFromGroup()
                    self.board[targetRow-2][self.possibleCol[targetCol]]=None

                elif self.color == 'WHITE' and self.board[targetRow][self.possibleCol[targetCol]] in self.game.playerOnePassantPawns:
                    print('in white en passant captured')
                    self.board[targetRow][self.possibleCol[targetCol]].removeFromGroup()
                    self.board[targetRow][self.possibleCol[targetCol]]=None   

            #Check if the move created a candidate for inPassant capture
            if self.isPassant(preMoveRow,targetRow,targetCol):
                if self.color=='BLACK':
                    self.game.playerOnePassantPawns.add(self)
                else:
                    self.game.playerTwoPassantPawns.add(self)
            
            #Here I check if it is a candidate for a passant move first before I label hasMoved as true

            self.hasMoved=True
            self.game.turn[0]+=1
            
            print(self.game.turn[0])
            
        else:
            print("error FALSE MOVE")
            print(f' requested {targetRow,targetCol} but available moves are {self.availableMoves()} ALSO {len(self.availableMoves())==0}')
            print(self.__repr__())
            return False
