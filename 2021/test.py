a = [
    [False, False, False, False, False, False, True, True, True, False],
    [False, False, False, False, False, False, False, True, True, True],
    [False, False, False, False, False, False, False, False, True, True],
    [False, False, False, False, False, False, False, False, True, True],
    [False, False, False, False, False, False, False, True, True, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
]


def flatten(t):
    return [item for sublist in t for item in sublist]


print(all(flatten(a)))

