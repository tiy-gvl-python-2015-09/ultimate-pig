import random


class PigMoves(Opponent):

    def decision(self):
        if self.count > 0:
            return "hold"
        elif self.score == 0 and self.count > 0:
            return "bust"
        else:
            self.count += 1
            return "roll"
