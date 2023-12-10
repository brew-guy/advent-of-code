import time, math
from helpers import *

t = time.time()

# Input
t1, d1 = 61, 430
t2, d2 = 67, 1036
t3, d3 = 75, 1307
t4, d4 = 71, 1150

# Part 1

# function that solves the second degree equation for ax^2 + bx + c = n
def solve_quad(a, b, c, n):
    """
    Solves the equation ax^2 + bx + c = n for x
    """
    # Compute the discriminant
    d = b**2 - 4*a*(c-n)

    # Find the roots
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)

    return x1, x2

# For this problem, the equation seems to be d = -t^2 + tmax * t + 0
def solve_race(tmax, dmax):
    """
    Solves the equation d = -t^2 + tmax * t + 0 for t
    """
    time1, time2 = solve_quad(-1, tmax, 0, dmax)
    # Correct if solutions are integers since only solutions in
    # the interval between dmax are valid
    if int(time1) == time1: time1 += 1
    if int(time2) == time2: time2 -= 1
    interval = math.floor(time2) - math.ceil(time1) + 1
    return interval

s1 = solve_race(t1, d1)
s2 = solve_race(t2, d2)
s3 = solve_race(t3, d3)
s4 = solve_race(t4, d4)

dropstar(11, s1*s2*s3*s4, t)

# Part 2

# Input
t5 = 61677571
d5 = 430103613071150
s5 = solve_race(t5, d5)

dropstar(12, s5, t)
