#!/usr/bin/python3


""" Funct that count line by li"""
import sys


i = 0
FileSize = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
code = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        i += 1
        sp = line.split(' ')
        if len(sp) > 2:
            FileSize += int(sp[-1])
            if sp[-2] in stats:
                stats[sp[-2]] += 1
        if i % 10 == 0:
            print("File size: {}".format(FileSize))
            for f in code:
                if stats[f]:
                    print("{}: {}".format(f, stats[f]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(FileSize))
    for f in code:
        if stats[f]:
            print("{}: {}".format(f, stats[f]))
