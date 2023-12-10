import time
from helpers import *

t = time.time()

input = mypath + "d12-input.txt"
with open(input) as f:
    heightmap = [list(m) for m in f.read().split("\n")]

# Part 1
# Read input to 2D list of characters
# Locate S and E coordinate sets in input
# Adapt pathfinder algo to check for character value differences (height) and only allow move U/D/L/R
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, value=None):
        self.parent = parent
        self.position = position
        self.value = value

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start, maze[start[0]][start[1]])
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end, maze[end[0]][end[1]])
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        print(current_node.value)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # Make sure within range
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # Get 'height' of current node and new node
            node_value = maze[current_node.position[0]][current_node.position[1]]
            current_node_height = ord(node_value)
            new_node_height = ord(maze[node_position[0]][node_position[1]])

            # Make sure walkable terrain
            if new_node_height - current_node_height > 5:
                continue

            # Create new node
            new_node = Node(current_node, node_position, node_value)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                (child.position[1] - end_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# Start point and destination
start = [
    (x, y) for x, row in enumerate(heightmap) for y, col in enumerate(row) if col == "S"
][0]
end = [
    (x, y) for x, row in enumerate(heightmap) for y, col in enumerate(row) if col == "E"
][0]
heightmap[start[0]][start[1]] = "a"
heightmap[end[0]][end[1]] = "z"

path = astar(heightmap, start, end)
print(path)


dropstar(23, False, t)

# Part 2


dropstar(24, False, t)
