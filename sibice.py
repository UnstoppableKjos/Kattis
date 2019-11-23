#! /usr/bin/python3

import sys
import math

n, w, h = [int(c.rstrip()) for c in sys.stdin.readline().split()]

max_len = math.sqrt(w**2 + h**2)

for indx, match in enumerate(sys.stdin.readlines()):
    match = int(match.rstrip())
    if match <= max_len:
        print("DA")
    else:
        print("NE")
