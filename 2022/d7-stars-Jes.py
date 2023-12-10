import re
import time
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    terminal = f.read().split("\n")

# Part 1
# Split input to array of strings at linebreaks
# OOP solution: file class (type, name, size, parent), dir class (type, name, parent, children, size)
# Lexer?


class System:
    def __init__(self):
        self.children = []


class File:
    def __init__(self, name, size):
        self.type = "file"
        self.name = name
        self.size = size
        self.parent = None

    def __str__(self):
        return f"{self.name} ({self.type}, size={self.size})"


class Dir:
    def __init__(self, name, parent=None):
        self.type = "dir"
        self.name = name
        self.parent = parent
        self.size = 0
        self.totalsize = 0
        self.children = []

    def __str__(self):
        return f"{self.name} ({self.type}, size={self.size})"

    def update_parent(self, size):
        if self.parent != None:
            self.parent.totalsize += size

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        if child.type == "file":
            self.size += child.size
            self.totalsize += child.size
            self.update_parent(child.size)


d = Dir("root")
d2 = Dir("pictures")
d.add_child(d2)
f1 = File("pix.png", 345)
f2 = File("cup.png", 123)
d.add_child(f1)
d2.add_child(f2)
print(d2.parent)
print(d.size)
print(d.totalsize)

# current, parent = None, None
# for line in terminal:
#     cmd = line.split(" ")

#     if line.find("$ cd ") > -1:
#         if cmd[2] == "..":
#             current = parent
#         else:


dropstar(13, False, t)

# Part 2

dropstar(14, False, t)
