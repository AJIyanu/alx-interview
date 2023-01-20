#!/usr/bin/python3
"""Readvfrom stdin"""


import sys

file_size = []
status_code = {'200': 0, '301': 0, '400': 0,
               '401': 0, '403': 0, '404': 0,
               '405': 0, '500': 0
               }
count = 0
for line in sys.stdin:
    try:
        div = line.split()
        if len(div) != 9:
            continue
        count += 1
        try:
            file_size.append(int(div[8]))
        except Exception:
            continue
        code = div[7]
        if code in status_code:
            status_code[code] += 1
        else:
            file_size.pop()
            count -= 1
            continue
        if count == 10:
            file_size = [sum(file_size)]
            print("File size: {}".format(file_size[0]))
            for cod in status_code:
                if status_code[cod] != 0:
                    print("{}: {}".format(int(cod), status_code[cod]))
            count = 0
    except KeyboardInterrupt:
        break

print("File size:", sum(file_size))
for cod in status_code:
    if status_code[cod] != 0:
        print("{}: {}".format(cod, status_code[cod]))
