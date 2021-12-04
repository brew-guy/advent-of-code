a = [
    ["x", 1, 54, 92, 80],
    ["x", 50, 11, 27, 78],
    ["x", 9, 25, 38, 20],
    ["x", 90, 39, 37, 15],
    [87, 87, 87, 87, 87],
]


def boardSum(board):
    return [n for row in board for n in row if isinstance(n, int)]


print(a)
b = [["x" if x == 1 else x for x in row] for row in a]
print(b)
print(boardSum(a))
