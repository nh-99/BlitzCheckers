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
                elif (x + 2) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[94m'))
            elif i == 1 or i == 6:
                if (x + 1) % 2 and i < 3:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[91m'))
                elif (x + 1) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i), '\033[94m'))


def get_piece(location):
    for piece in gamepieces:
        if piece.get_location() == location:
            return piece
    return None


def valid_move(is_blue, old_location, new_location):
    if is_blue:
        piece1 = get_piece(old_location)
        piece2 = get_piece(new_location)

        if not piece1:
            return False

        if not piece1.get_team() == '\033[94m':
            return False

        location = piece1.get_location()
        print location.split()
        test_locations = [str(int(location[0]) + 1) + str(int(location[1]) - 1), str(int(location[0]) - 1) + str(int(location[1]) - 1)]
        for loc in test_locations:
            if loc == new_location:
                if not piece2:
                    return True

        return False


def move_piece(command):
    locations = command.split(' ')
    piece = get_piece(str(locations[0][1]) + str(ord(locations[0][0].lower()) - 97))
    if piece:
        if valid_move(True, piece.get_location(), str(locations[2][1]) + str(ord(locations[2][0].lower()) - 97)):
            piece.move_piece(str(locations[2][1]) + str(ord(locations[2][0].lower()) - 97))
            return True
        else:
            return False
    else:
        return False
