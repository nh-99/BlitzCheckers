import gamepiece
header = '     0   1   2   3   4   5   6   7'
footer = '   +---+---+---+---+---+---+---+---+'


def construct_board():
    print("\n" * 100)
    print header
    print footer

    for y in range(0, 8):
        to_print = str(y) + '  '
        for x in range(0, 9):
            piece = gamepiece.get_piece(str(x) + str(y))
            if piece:
                to_print += '| ' + piece.get_team() + 'O\033[0m '
            else:
                to_print += '|   '
        print to_print
        print footer


def init_board():
    gamepiece.init_pieces()
    construct_board()


def update_board():
    construct_board()

gamepiece.init_pieces()
construct_board()
