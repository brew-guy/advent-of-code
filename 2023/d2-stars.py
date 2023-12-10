import time, re, functools
from helpers import *

t = time.time()

input = mypath + "d2-input.txt"
with open(input) as f:
    games = f.read().split("\n")

# Part 1
# Function that splits a game string into its components
# Store game id, red, green, blue cubes in array
# Sort the game ids that adhere to the rules

def split_draw(draw):
    cubes = re.findall(r"(\d+) (\w+)", draw)
    r = sum([int(c[0]) for c in cubes if c[1] == "red"])
    g = sum([int(c[0]) for c in cubes if c[1] == "green"])
    b = sum([int(c[0]) for c in cubes if c[1] == "blue"])
    return (r, g, b)

def split_game(game):
    game_id = int(re.match(r"Game (\d+):", game).groups()[0])
    draws = game.split(":")[1].split(";")
    draws = [split_draw(draw.strip()) for draw in draws]
    return [game_id, draws]

rules = (12,13,14)


ids = []
for game in games:
    game_id, draws = split_game(game)
    # reduce array of tuples to single tuple with max values
    max_cubes = functools.reduce(lambda a, b: tuple(max(x) for x in zip(a, b)), draws)
    # sort game ids that adhere to the rules
    if max_cubes[0] <= rules[0] and max_cubes[1] <= rules[1] and max_cubes[2] <= rules[2]:
        ids.append(game_id)

dropstar(3, sum(ids), t)

# Part 2
# repeat part 1 game loop and disregard the rules

power = []
for game in games:
    game_id, draws = split_game(game)
    # reduce array of tuples to single tuple with max values
    max_cubes = functools.reduce(lambda a, b: tuple(max(x) for x in zip(a, b)), draws)
    product = lambda x: functools.reduce(lambda a, b: a * b, x)
    power.append(product(max_cubes))

dropstar(4, sum(power), t)
