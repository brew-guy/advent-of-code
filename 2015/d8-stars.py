import time, re
from helpers import *

t = time.time()

input = mypath + "d8-input.txt"
with open(input) as f:
    strings = f.read().split("\n")

# Part 1
def escape(str):
    str = str[1:-1].replace(chr(92) + chr(92), chr(92))  # \\ -> \
    str = str.replace(chr(92) + chr(34), chr(34))  # \" -> "
    str = re.sub(r"\\x([a-f0-9]{2})", r".", str)  # Fake ASCII replacement :(
    return str


code_size = [len(s) for s in strings]
mem_size = [len(escape(s)) for s in strings]

dropstar(15, sum(code_size) - sum(mem_size), t)

# Part 2
def encode(str):
    str = str.replace(chr(92), chr(92) + chr(92))  # \ -> \\
    str = str.replace(chr(34), chr(92) + chr(34))  # " -> \"
    str = chr(34) + str + chr(34)  # Enclose in double quotes
    return str


enc_size = [len(encode(s)) for s in strings]

dropstar(16, sum(enc_size) - sum(code_size), t)

