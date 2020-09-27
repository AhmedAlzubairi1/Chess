'''
This is a general class to describe the characteristics that every piece should have
'''

class Piece():
    def __init__(self,board,group,name,row,col):
        possiblePieces={'Pawn','Rook','Knight','King','Queen','Bishop'}
        self.possibleRow={i:i-1 for i in range(1,9)}
        self.possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
        #Check they are valid
        assert name in possiblePieces , f"Invalid pawn type. Make sure name is one of {possiblePieces}"
        assert col in self.possibleCol , f"Invalid column location, make sure it is between A and H (inclusive and uppercase)"
        assert row in self.possibleRow , f"Invalid row location, make sure it is between 1 and 8 (inclusive)"
        self.board=board
        self.group=group
        self.name=name
        self.row=row
        self.col=col

    def availableMoves(self):
        #Returns a set of the avaiable moves the piece can make
        pass

    def checkIfNotNearKing(self,row,col):
        #TODO this should check if the location is a king or near a king. If it is, return False. Else return True
        pass
    
    def move(self,targetRow,targetCol):
        #Example input : 1A for bottom left location 
        if (targetRow-1,self.possibleCol[targetCol]) in self.availableMoves():
            #Check if there is already a piece there. If so, remove it and replace
            if self.board[targetRow-1,self.possibleCol[targetCol]] is not None:
                self.board[targetRow-1,self.possibleCol[targetCol]].removeFromGroup()
                self.row=targetRow
                self.col=targetCol
                self.board[targetRow-1,self.possibleCol[targetCol]]=self
            else:
                #Else, just move it to that location
                self.row=targetRow
                self.col=targetCol
                self.board[targetRow-1,self.possibleCol[targetCol]]=self
        else:
            return False

    def removeFromGroup(self):
        #This removes the piece from the current player's set
        self.group.remove(self)
    
    def __repr__(self):
        return f'{self.name}-{self.row}{self.col}' 

#Ignoe
'''
class temp(piece):
    def __init__(self,group,name,row,col):
        super().__init__(group,name,row,col)
'''