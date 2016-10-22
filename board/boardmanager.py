import gamepiece
header = '     0   1   2   3   4   5   6   7'
footer = '   +---+---+---+---+---+---+---+---+'


def construct_board():
    print("\n" * 100)
    print header
    print footer

    for i in range(0, 8):
        to_print = str(i)
        for x in range(0, 9):
            to_print += '  | '
        print to_print
        print footer

    for piece in gamepiece.gamepieces:
        print piece.location


def init_board():
    gamepiece.init_pieces()
    construct_board()


def update_board():
    construct_board()

construct_board()