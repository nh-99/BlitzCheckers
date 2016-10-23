import re
from board import gamepiece, boardmanager
player_score = 0


def handle_move():
    global player_score

    new_move = raw_input('What is your next move?\n')
    if new_move:
        if new_move.lower() == "quit":
            print "Thank you for playing!"
            return

        parsed_input = re.search('([A-Z][0-9]) to ([A-Z][0-9])', new_move)
        try:
            parsed_input.group(0)
            parsed_input.group(1)
            is_move = gamepiece.move_piece(parsed_input.group(0) + ' to ' + parsed_input.group(1))
            if is_move:
                if is_move == 'jump':
                    player_score += 1
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

gamepiece.init_pieces()
boardmanager.construct_board()
handle_move()
