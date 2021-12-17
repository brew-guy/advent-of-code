map = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 22, 33, 44, 55], [66, 77, 88, 99, 00]]


def adjacent(matrix, row, col):
    dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
    adjacents = []
    for i in range(4):
        ax, ay = row + dy[i], col + dx[i]
        if min(ax, ay) >= 0 and ax < len(matrix) and ay < len(matrix[0]):
            adjacents.append([ax, ay])
    return adjacents


print(adjacent(map, 1, 1))

