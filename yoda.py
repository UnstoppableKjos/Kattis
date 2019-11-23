#! /usr/bin/python3
import sys

# Get the numbers
a, b = [line.rstrip() for line in sys.stdin.readlines()]

# Reverse the numbers
a = a[::-1]
b = b[::-1]

# Results go here
ra = ""
rb = ""

# Collide each digit
for i, x in enumerate(a):
    try:
        if int(x) > int(b[i]):
            ra += x
        elif int(x) == int(b[i]):
            ra += x
            rb += x
        else:
            rb += b[i]
    except IndexError:  # If a number is shorter than the other, the longer keeps the remaining digits
        if len(a) > len(b):
            ra += a[i:]
        else:
            ra += b[i:]

# Reverse the numbers back if it has digits, otherwise, make it YODA
if len(ra) > 0:
    ra = int(ra[::-1])
else:
    ra = "YODA"
if len(rb) > 0:
    rb = int(rb[::-1])
else:
    rb = "YODA"

# Prints results
print(ra)
print(rb)
