#!/usr/bin/python3
"""
Utf-8 validation code
"""


def validUTF8(data):
    """returns true if valid false if not"""
    count = 0
    for check in data:
        if count == 3 or count == 2 or count == 1:
            if check > 192 or check < 128:
                return False
            count -= 1
        else:
            if check > 255:
                return False
            if check > 239:
                if check == 240:
                    return False
                count = 3
            elif check > 223:
                if check == 224:
                    return False
                count = 2
            elif check > 191:
                if check == 192:
                    return False
                count = 1
            elif check > 127:
                return False
            else:
                count = 0
    return True
