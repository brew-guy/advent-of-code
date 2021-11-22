import time, hashlib
from helpers import *

t = time.time()

secret_key = "iwrupvqb"

# Part 1
i, md5hex = 0, ""
while md5hex[:5] != "00000":
    key_iteration = secret_key + str(i)
    md5 = hashlib.md5(key_iteration.encode())
    md5hex = md5.hexdigest()
    i += 1

dropstar(7, i - 1, t)

# Part 2
i, md5hex = 0, ""
while md5hex[:6] != "000000":
    key_iteration = secret_key + str(i)
    md5 = hashlib.md5(key_iteration.encode())
    md5hex = md5.hexdigest()
    i += 1

dropstar(8, i - 1, t)
