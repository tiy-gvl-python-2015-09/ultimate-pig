import random


class PigMoves(Opponent):

    def decision(self):
        if self.score > 13:
            return "hold"
        elif self.score == 0 and self.count > 0:
            return "bust"
        else:
            self.count += 1
            return "roll"

class Game:

    def __init__(self):
        self.p1 = Player()
        self.p2 = Opponent()
        self.round_count = 0

    def pick_first(self):
        guess = input("Pick heads or tails. ").lower()
        coin_toss = random.choice(['heads', 'tails'])
        if guess == coin_toss:
            print("You go first.")
            return True
        elif guess != 'heads' and guess != 'tails':
            print("Fine, wise guy. Your opponent goes first")
            return False
        else:
            print("Your opponent goes first.")
            return False

    def p1_turn(self):
        self.p1.roll_or_hold()

    def p2_turn(self):
        self.p2.roll_or_hold()

    def play_round_me(self):
            self.p1_turn()
            self.p2_turn()

    def play_round_you(self):
            self.p2_turn()
            self.p1_turn()

    def full_game(self):
        pick = self.pick_first()
        if pick == True:
            while self.round_count < 7:
                self.play_round_me()
                self.round_count += 1
            self.win_lose()
        if pick == False:
            while self.round_count < 7:
                self.play_round_you()
                self.round_count += 1
            self.win_lose()

    def win_lose(self):
        if self.p1.total_score > self.p2.total_score:
            return "YOU WIN! Final score is {}, to {}.".format(
            self.p1.total_score, self.p2.total_score)
        else:
            return "YOU LOSE! Final score is {}, to {}.".format(
            self.p1.total_score, self.p2.total_score)

play_game = Game()
play_game.full_game()
