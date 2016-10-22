gamepieces = []


class GamePiece:
    location = '00'
    team = 'red'

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
                if (x + 1) % 2 and i < 3:
                    gamepieces.append(GamePiece(str(x) + str(i), 'red'))
                else:
                    gamepieces.append(GamePiece(str(x) + str(i), 'black'))
            elif i == 1 or i == 6:
                if (x + 2) % 2 and i < 3:
                    gamepieces.append(GamePiece(str(x) + str(i), 'red'))
                else:
                    gamepieces.append(GamePiece(str(x) + str(i), 'black'))
