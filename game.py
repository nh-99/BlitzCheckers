from board import gamepiece, boardmanager
import re, sys
from colorama import init, Fore, Back, Style
init()
player_score = 0


def main_menu():
    print Fore.CYAN + "______ _ _ _       _____ _               _"
    print "| ___ \ (_) |     /  __ \ |             | |                "
    print "| |_/ / |_| |_ ___| /  \/ |__   ___  ___| | _____ _ __ ___ "
    print "| ___ \ | | __|_  / |   | '_ \ / _ \/ __| |/ / _ \ '__/ __|"
    print "| |_/ / | | |_ / /| \__/\ | | |  __/ (__|   <  __/ |  \__ \\"
    print "\____/|_|_|\__/___|\____/_| |_|\___|\___|_|\_\___|_|  |___/" + Fore.RESET
    print
    print Back.BLUE + 'By Noah Howard' + Back.RESET
    print
    print 'Welcome to BlitzCheckers! To play, enter 1. For instructions, enter 2.'
    choice = raw_input()
    if choice:
        if choice == '1':
            gamepiece.init_pieces()
            boardmanager.construct_board()
            handle_move()
        elif choice == '2':
            print '\n' * 100
            print 'The primary objective of this game is to move all your pieces to the other end of the board.'
            print 'In order to score more points, you may jump enemy checkers for an extra point each.'
            print 'You may only jump one checker at a time.'
            print ''
            print 'Getting a piece to the other side gives you 10 points. Once all the pieces are at the other'
            print 'end, you have won the game.'
            print ''
            main_menu()
        else:
            print 'The choice you entered is invalid. Please try a different one.'
            main_menu()


def reset_game():
    global player_score
    player_score = 0
    gamepiece.init_pieces()
    boardmanager.construct_board()
    handle_move()


def do_win():
    print 'Congratulations, you won! Thank you for playing!'
    yes_no = raw_input('Would you like to play again? (y/n)\n')
    if yes_no == 'y':
        reset_game()
    elif yes_no == 'n':
        sys.exit()
    else:
        print 'Please enter valid y or n'
        do_win()


def handle_move():
    global player_score

    print 'Your score is currently ' + Fore.GREEN + str(player_score) + Style.RESET_ALL
    new_move = raw_input('What is your next move? (Format like ' + Style.BRIGHT + 'F0 to E1' + Style.NORMAL + ', or enter quit to exit)\n')
    if new_move:
        if new_move.lower() == "quit":
            print "Thank you for playing!"
            return

        parsed_input = re.search('([A-Z][0-7]) to ([A-Z][0-7])', new_move)
        try:
            parsed_input.group(0)
            parsed_input.group(1)
            is_move = gamepiece.move_piece(parsed_input.group(0) + ' to ' + parsed_input.group(1))
            if is_move:
                if is_move == 'jump':
                    player_score += 1
                elif is_move == 'win1':
                    player_score += 10
                elif is_move == 'win2':
                    print '\n' * 100
                    do_win()
                elif is_move == 'win3':
                    print '\n' * 100
                    print 'Sorry, but you did not win this round. Feel free to try again!'
                boardmanager.construct_board()
                handle_move()
            else:
                boardmanager.construct_board()
                print 'That move is invalid. Please try again'
                handle_move()
        except AttributeError:
            boardmanager.construct_board()
            print 'Invalid command (format the command like "A0 to B0")'
            handle_move()
    else:
        boardmanager.construct_board()
        print 'Invalid command (format the command like "A0 to B0")'
        handle_move()

main_menu()
