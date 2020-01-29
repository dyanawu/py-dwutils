#! /usr/bin/python3

import sys

ins = sys.stdin.read()
[x, y] = [int(i) for i in ins.split()]

if x*y > 0:
    print(1) if x > 0 else print(3)
else:
    print(4) if x > 0 else print (2)
