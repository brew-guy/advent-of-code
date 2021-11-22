import time, re
from helpers import *

t = time.time()

password = "hepxcrrq"
# Part 1
def hasTriplet(string):
    for idx, c in enumerate(string[:-2]):
        if ord(c) == ord(string[idx + 1]) - 1 and ord(c) == ord(string[idx + 2]) - 2:
            return True
    return False


def hasNoIOL(string):
    regexp = re.compile(r"[iol]")
    match = re.search(regexp, string)
    return match == None


def hasTwoPairs(string):
    regexp = re.compile(r"(.)\1")
    match = re.findall(regexp, string)
    return len(match) > 1 and len(match) == len(set(match))


def incrementPW(password, carry=None, output=""):
    if len(password) < 1 or carry == False:
        return output
    else:
        letter = password[-1]
        if letter == "z":
            output = "a" + output
            carry = True
        else:
            output = password[:-1] + chr(ord(password[-1]) + 1) + output
            carry = False
        return incrementPW(password[:-1], carry, output)


def findNextValidPW(password):
    valid = False
    while not valid:
        password = incrementPW(password)
        validation_matrix = [
            hasNoIOL(password),
            hasTwoPairs(password),
            hasTriplet(password),
        ]
        # print(password, validation_matrix)
        valid = all(validation_matrix)
    return password


nextpass = findNextValidPW(password)
dropstar(21, nextpass, t)

# Part 2
password = nextpass
nextpass = findNextValidPW(password)

dropstar(22, nextpass, t)
