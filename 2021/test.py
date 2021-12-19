import itertools

x = range(1, 10)
i = [p for p in itertools.product(x, repeat=2)]
for _ in i:
    print(_)

