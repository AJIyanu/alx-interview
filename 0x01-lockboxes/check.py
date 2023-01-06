#!/usr/bin/python3

canUnlockAll = __import__('temp').canUnlockAll

if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print("Done creating list")
    print(canUnlockAll(boxes))
