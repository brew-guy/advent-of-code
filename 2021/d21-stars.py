import time, re
from helpers import *

t = time.time()

input = mypath + "d21-input.txt"
with open(input) as f:
    players = f.read()

p_pos = re.findall("Player \d starting position: (\d)", players)
p1_pos, p2_pos = [int(pos) for pos in p_pos]

# Part 1
class Det_dice:
    def __init__(self) -> None:
        self.eyes = 0
        self.rolls = 0

    def roll(self):
        self.eyes = self.eyes % 100 + 1
        self.rolls += 1
        return self.eyes


class Player:
    def __init__(self, start_pos) -> None:
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.score = 0
        self.moves = []

    def move(self, roll):
        new_pos = (self.current_pos + roll - 1) % 10 + 1
        self.moves.append({"roll": roll, "score": new_pos})
        self.current_pos = new_pos
        self.score += new_pos


die = Det_dice()
p1 = Player(p1_pos)
p2 = Player(p2_pos)

while True:
    if p1.score < 1000 and p2.score < 1000:
        roll = die.roll() + die.roll() + die.roll()
        p1.move(roll)
    else:
        break

    if p1.score < 1000 and p2.score < 1000:
        roll = die.roll() + die.roll() + die.roll()
        p2.move(roll)
    else:
        break

dropstar(41, min(p1.score, p2.score) * die.rolls, t)

# Part 2
# 3 rolls => 3^3=27 new realities. Frequency of the rolls across the 27?
rolls_dict = {}

# dropstar(42, , t)
