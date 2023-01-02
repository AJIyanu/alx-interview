#!/usr/bin/python3
"""interview question module
locked boxes
"""


def canUnlockAll(boxes):
    """check if all boxes can be unlocked"""
    valid = []
    for n in range(len(boxes)):
        valid.append("locked")
    valid[0] = "unlocked"
    for i in range(len(valid)):
        for check in range(len(valid)):
            if valid[check] == "unlocked":
                getkey = boxes[check]
            for i in getkey:
                valid[i] = "unlocked"
    for validate in valid:
        if validate == "locked":
            return (False)
    return (True)
