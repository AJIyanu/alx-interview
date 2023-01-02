#!/usr/bin/python3
"""check code"""
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
boxes1 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
boxes2 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes2))
print(canUnlockAll(boxes1))
print(boxes)
print(canUnlockAll(boxes))
