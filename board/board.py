from . import gamepiece

def construct_board():
    print(chr(27) + "[2J")
    for piece in gamepiece.gamepieces:
        print piece.location
