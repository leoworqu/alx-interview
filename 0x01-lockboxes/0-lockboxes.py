#!/usr/bin/python3
"""
Determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)