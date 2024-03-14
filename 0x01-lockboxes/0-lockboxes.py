#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked"""

    def explore(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                stack.append(key)

    if not boxes or not boxes[0]:
        return False

    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        explore(current_box)

    return len(visited) == len(boxes)
