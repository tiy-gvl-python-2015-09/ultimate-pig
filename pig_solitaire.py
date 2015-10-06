import random

class Dice:

    def roll(self):
        roll = random.randint(1,6)
        return roll


class Opponent:

    def __init__(self):
        self.dice = Dice()
        self.score = 0
        self.total_score = 0
        self.count = 0


    def roll(self):
        return self.dice.roll()

    def round_score(self):
        roll = self.roll()
        if roll > 1:
            self.score += roll
        else:
            self.score = 0

        return self.score

    def roll_or_hold(self):
        response = self.decision()
        self.decision()
        if response == 'hold':
            print("\nYour opponant holds")
            self.total_score += self.score
            self.score = 0
            self.count = 0
            return self.total_score
        elif response == 'roll':
            print("\nYour opponant rolls")
            self.round_score()
            print("your opponents score this round: ", self.score)
            print("your opponents total score: ", self.total_score)
            return self.roll_or_hold()
        elif response == 'bust':
            print("\nYour opponant busts")
            self.count = 0
            return self.total_score

    def decision(self):
        if self.count > 0:
            return "hold"
        elif self.score == 0 and self.count > 0:
            return "bust"
        else:
            self.count += 1
            return "roll"


class Player:

    def __init__(self):
        self.dice = Dice()
        self.score = 0
        self.total_score = 0
        self.count = 0

    def roll(self):
        return self.dice.roll()

    def round_score(self):
        roll = self.roll()
        if roll > 1:
            self.score += roll
        else:
            self.score = 0
        return self.score

    def roll_or_hold(self):
        if self.score == 0 and self.count > 0:
            print(self.count)
            print("You bust")
            self.count = 0
            return self.total_score
        else:
            response = input(
            "\nDo you want to roll or hold? (Roll/Hold)".lower())
            if response == 'hold':
                print("You hold")
                self.total_score += self.score
                self.score = 0
                self.count = 0
                return self.total_score
            if response == 'roll':
                print("You roll")
                self.round_score()
                print("your score this round: ", self.score)
                print("your total score: ", self.total_score)
                self.count += 1
                return self.roll_or_hold()

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
