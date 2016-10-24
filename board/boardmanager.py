from colorama import Style, Fore
import gamepiece
header = '     0   1   2   3   4   5   6   7'
footer = '   +---+---+---+---+---+---+---+---+'


def construct_board():
    print("\n" * 100)
    
    print Fore.CYAN + "______ _ _ _       _____ _               _"
    print "| ___ \ (_) |     /  __ \ |             | |                "
    print "| |_/ / |_| |_ ___| /  \/ |__   ___  ___| | _____ _ __ ___ "
    print "| ___ \ | | __|_  / |   | '_ \ / _ \/ __| |/ / _ \ '__/ __|"
    print "| |_/ / | | |_ / /| \__/\ | | |  __/ (__|   <  __/ |  \__ \\"
    print "\____/|_|_|\__/___|\____/_| |_|\___|\___|_|\_\___|_|  |___/" + Fore.RESET
    print
    print
    print header
    print footer

    for y in range(0, 8):
        to_print = chr(y + 97).upper() + '  '
        for x in range(0, 9):
            piece = gamepiece.get_piece(str(x) + str(y))
            if piece:
                to_print += '| ' + piece.get_team() + 'O' + Style.RESET_ALL + ' '
            else:
                to_print += '|   '
        print to_print
        print footer


def init_board():
    gamepiece.init_pieces()
    construct_board()


def update_board():
    construct_board()
