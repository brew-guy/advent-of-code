import time
from helpers import *

t = time.time()

a = eval("lambda x: x * 9")

count = 0
for i in range(10000):

    count += a(i)


dropstar(1, count, t)
