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
        print("working here", valid[i], i)
        for check in range(len(valid)):
            print(check, "also working here")
            if valid[check] == "unlocked":
                getkey = boxes[check]
                print(getkey, "we are unlocking these boxes now")
            for i in getkey:
                valid[i] = "unlocked"
            print(valid)
    #print(valid)
    for validate in valid:
        if validate == "locked":
            return (False)
    return (True)
