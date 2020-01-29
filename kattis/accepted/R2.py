#! /usr/bin/python3

import sys

ins = sys.stdin.read()
r1, s1 = ins.split()
r2 = int(s1) * 2 - int(r1)

print(r2)
