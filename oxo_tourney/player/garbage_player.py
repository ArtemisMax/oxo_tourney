from oxo_tourney.player.player import Player

# Create new player class from this template
# Add a line for your player class to the __init__.py file
# Implement your version of the get_move function


class GarbagePlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.row = 0
        self.col = 0

    def get_move(self, board, symbol=None):
        self.row = self.row + 1
        if self.row > board.size:
            self.row = 0
            print("I'm getting closer to a bingo!")
            self.col = self.col + 1
            if self.col > board.size:
                self.col = 0
                print('Bingo!!!!!')

        return [self.row, self.col]