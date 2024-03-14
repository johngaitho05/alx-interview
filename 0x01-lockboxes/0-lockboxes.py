#!/usr/bin/python3

def canUnlockAll(boxes):
    def explore(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                stack.append(key)

    if not boxes:
        return True

    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        explore(current_box)

    return len(visited) == len(boxes)

