gamepieces = []


class GamePiece:
    location = '00'

    def __init__(self, location):
        self.location = location

    def move_piece(self, location):
        self.location = location

    def get_location(self):
        return self.location


def init_pieces():
    for i in range(0, 3):
        for x in range(0, 8):
            if i == 0 or i == 2:
                if (x + 1) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i)))
            else:
                if (x + 2) % 2:
                    gamepieces.append(GamePiece(str(x) + str(i)))

init_pieces()
for piece in gamepieces:
    print piece.get_location()
