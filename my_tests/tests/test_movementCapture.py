from sys import path
from os.path import dirname as dir
path.append(dir(path[0])[0:dir(path[0]).rfind('\\')])
# I did this to make sure it is appending c:\Users\Ahmed Alzubairi\Documents\Open Source\COMS4995

from  Pieces.Bishop import Bishop

def test_sub():
    assert 33 == 33
