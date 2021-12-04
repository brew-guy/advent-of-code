import time
from helpers import *

t = time.time()

input = mypath + "d4-input.txt"
with open(input) as f:
    bingo = [b for b in f.read().split("\n\n")]

numbers = [int(n) for n in bingo[0].split(",")]
boards = [[int(n) for n in " ".join(b.split("\n")).split()] for b in bingo[1:]]
boards = [[b[i : i + 5] for i in range(0, len(b), 5)] for b in boards]


def makeBoard(board):
    return "\n".join(
        [
            " ".join([str(i) if len(str(i)) == 2 else " " + str(i) for i in r])
            for r in board
        ]
    )


# Part 1
def transpose(board):
    return list(zip(*board))


def hasBingo(board):
    row = [b.count(b[0]) == len(b) for b in board]
    col = [b.count(b[0]) == len(b) for b in transpose(board)]
    return any(row) or any(col)


def boardSum(board):
    return sum([n for row in board for n in row if isinstance(n, int)])


bingo_on, i = True, 0
while bingo_on:
    number = numbers[i]
    for idx, board in enumerate(boards):
        boards[idx] = [["x" if x == number else x for x in row] for row in board]
        if hasBingo(boards[idx]):  # stop on first board with bingo
            bingo_on = False
            break
    i += 1

final_score = boardSum(boards[idx]) * number

dropstar(1, final_score, t)

# Part 2
bingo_on, i = True, 0
had_bingo = []
while bingo_on:
    number = numbers[i]
    for idx, board in enumerate(boards):
        boards[idx] = [["x" if x == number else x for x in row] for row in board]
        if hasBingo(boards[idx]):
            if idx not in had_bingo:
                had_bingo.append(idx)
            if len(had_bingo) == len(boards):  # stop on last board with bingo
                bingo_on = False
                break
    i += 1

final_score = boardSum(boards[idx]) * number

dropstar(2, final_score, t)
