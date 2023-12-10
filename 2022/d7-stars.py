import time
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    terminal = f.read().split("\n")

# Part 1
# Split input to array of strings at linebreaks
# OOP solution: file class (type, name, size, parent), dir class (type, name, parent, children, size)


class System:
    def __init__(self):
        self.dirs = []

    def add_dir(self, dir):
        self.dirs.append(dir)

    def get_dir(self, name, parent):
        f = list(
            filter(lambda dir: dir.name == name and dir.parent == parent, self.dirs)
        )
        return f[0]


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
        self.root = False
        self.name = name
        self.parent = parent
        self.size = 0
        self.totalsize = 0
        self.children = []

    def __str__(self):
        return f"{self.name} ({self.type}, size={self.size}, total={self.totalsize})"

    def update_parent(self, size):
        if self.parent != None:
            self.parent.totalsize += size
            self.parent.update_parent(size)  # update parents recursively

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        if child.type == "file":
            self.size += child.size
            self.totalsize += child.size
            self.update_parent(child.size)


def getLine(input_lines):
    next_line = input_lines.pop(0)
    return next_line, input_lines


# Generate dir and file objects
next_line, remaining = None, terminal.copy()
root, current, parent = None, None, None
system = System()

while len(remaining) > 0:
    next_line, remaining = getLine(remaining)
    if next_line == "$ ls":
        while next_line.find("$ cd") == -1 and len(remaining) > 0:
            next_line, remaining = getLine(remaining)
            file_details = next_line.split(" ")
            if file_details[0] == "dir":
                system.add_dir(Dir(file_details[1], current))
            if file_details[0].isnumeric():
                current.add_child(File(file_details[1], int(file_details[0])))
    if next_line.find("$ cd") != -1:
        cmd_parts = next_line.split(" ")
        if cmd_parts[2] == "/":
            root = current = Dir("/")
            # system.add_dir(current)
        elif cmd_parts[2] == "..":
            current = current.parent
        else:
            parent = current
            current = system.get_dir(cmd_parts[2], current)

directories = [d.totalsize for d in system.dirs if d.totalsize <= 100_000]

dropstar(13, sum(directories), t)

# Part 2
# Calculate required space to be freed up
# Sort all dir sizes and find the nearest at or above the needed size to delete
t = time.time()

disk_size = 70_000_000
required = 30_000_000
free_size = disk_size - root.totalsize
still_needed = required - free_size

directories = sorted([d.totalsize for d in system.dirs if d.totalsize >= still_needed])

dropstar(14, directories[0], t)
