'''
This is a general class to describe the characteristics that every piece should have
'''

class piece():
    def __init__(self,group,name,row,col):
        possiblePieces={'Pawn','Rook','Knight','King','Queen','Bishop'}
        possibleRow={i:i-1 for i in range(1,9)}
        possibleCol={chr(i):i-ord('A') for i in range(ord('A'),ord('A')+8)}
        
        #Check they are valid
        assert name in possiblePieces , f"Invalid pawn type. Make sure name is one of {possiblePieces}"
        assert col in possibleCol , f"Invalid column location, make sure it is between A and H (inclusive and uppercase)"
        assert row in possibleRow , f"Invalid row location, make sure it is between 1 and 8 (inclusive)"

        self.group=group
        self.name=name
        self.row=row
        self.col=col

    def availableMoves():
        #Returns a set of the avaiable moves the piece can make
        pass

    def removeFromGroup(self):
        #This removes the piece from the current player's set
        self.group.remove(self)
    
    def __repr__(self):
        return f'{self.name}-{self.col}{self.row}' 

#Ignoe
'''
class temp(piece):
    def __init__(self,group,name,row,col):
        super().__init__(group,name,row,col)
'''