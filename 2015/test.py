from itertools import groupby


def lookandsay(number):
    return "".join(str(len(list(g))) + k for k, g in groupby(number))


numberstring = "3"
for i in range(55):
    numberstring = lookandsay(numberstring)

print(len(numberstring))
