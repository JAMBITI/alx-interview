#!/usr/bin/python3
"""for functions canUnlockAll"""


def canUnlockAll(boxes):
    """Check if it's possible to unlock all boxes"""
    opened = [0]
    for box in opened:
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(boxes) == len(opened):
        return True
    return False
