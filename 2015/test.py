n = 5


def sumInts(first, last):
    n = last - first + 1
    return n * (first + last) / 2


def sumIters(first, n):
    return n * (n + 2 * first - 1) / 2


r, c = 2, 5
i = sumInts(1, c)
j = summie(c, r - 1)

print(i, j)

