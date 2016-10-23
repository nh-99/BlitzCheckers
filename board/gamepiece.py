import random
gamepieces = []


class GamePiece:
    location = '00'
    team = '\033[91m'  # Define the team as a color, that way it's easier to print. This requires less code

    def __init__(self, location, team):
        self.location = location
        self.team = team

    def move_piece(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_team(self):
        return self.team


def init_pieces():
    for i in range(0, 8):
        for x in range(0, 8):
            if i == 0 or i == 2 or i == 5 or i == 7:
                if (x + 2) % 2 and i < 3:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[91m'))
                elif i > 4 and (x + 1) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[94m'))
            elif i == 1 or i == 6:
                if (x + 1) % 2 and i < 3:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[91m'))
                elif i > 4 and (x + 2) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[94m'))


def get_piece(location):
    for piece in gamepieces:
        if piece.get_location() == location:
            return piece
    return None


def get_team_pieces(team):
    to_return = []
    for piece in gamepieces:
        if piece.get_team() == team:
            to_return.append(piece)
    return to_return


def valid_move(is_blue, old_location, new_location):
    if is_blue:
        piece1 = get_piece(old_location)
        piece2 = get_piece(new_location)

        if not piece1:
            return False

        if not piece1.get_team() == '\033[94m':
            return False

        location = piece1.get_location()
        test_locations = [str(int(location[0]) + 1) + str(int(location[1]) - 1), str(int(location[0]) - 1) + str(int(location[1]) - 1)]
        for loc in test_locations:
            if loc == new_location:
                if not piece2:
                    return True
            else:
                if loc == str(int(location[0]) + 1) + str(int(location[1]) - 1):
                    if not piece2 and get_piece(loc) and piece1.get_location() == str(int(new_location[0]) - 2) + str(int(new_location[1]) + 2):
                        gamepieces.remove(get_piece(loc))
                        return 'jump'
                elif loc == str(int(location[0]) - 1) + str(int(location[1]) - 1):
                    if not piece2 and get_piece(loc) and piece1.get_location() == str(int(new_location[0]) + 2) + str(int(new_location[1]) + 2):
                        gamepieces.remove(get_piece(loc))
                        return 'jump'

        return False
    else:
        piece1 = get_piece(old_location)
        piece2 = get_piece(new_location)

        if not piece1:
            return False

        if not piece1.get_team() == '\033[91m':
            return False

        location = piece1.get_location()
        test_locations = [str(int(location[0]) + 1) + str(int(location[1]) + 1), str(int(location[0]) - 1) + str(int(location[1]) + 1)]
        for loc in test_locations:
            if loc == new_location:
                if not piece2:
                    return True
            else:
                if not get_piece(str(int(loc[0]) + 1) + str(int(loc[1]) - 1)):
                    gamepieces.remove(piece2)
                    return 'jump'

        return False


def bot_move():
    piece = random.choice(get_team_pieces('\033[91m'))
    x2_1 = int(piece.get_location()[0]) + 1
    x2_2 = int(piece.get_location()[0]) - 1
    y2 = int(piece.get_location()[1])

    if valid_move(False, piece.get_location(), str(x2_1) + str(y2)):
        piece.move_piece(str(x2_1) + str(y2))
    elif valid_move(False, piece.get_location(), str(x2_2) + str(y2)):
        piece.move_piece(str(x2_2) + str(y2))
    else:
        bot_move()


def move_piece(command):
    locations = command.split(' ')
    piece = get_piece(str(locations[0][1]) + str(ord(locations[0][0].lower()) - 97))
    if piece:
        is_valid = valid_move(True, piece.get_location(), str(locations[2][1]) + str(ord(locations[2][0].lower()) - 97))
        if is_valid:
            if is_valid == 'jump':
                piece.move_piece(str(locations[2][1]) + str(ord(locations[2][0].lower()) - 97))
                return 'jump'
            piece.move_piece(str(locations[2][1]) + str(ord(locations[2][0].lower()) - 97))
            #bot_move()
            return True
        else:
            return False
    else:
        return False
