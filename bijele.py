
import fileinput

p = [1, 1, 2, 2, 2, 8]

for line in fileinput.input():
    a = [int(n) for n in line.split()]
    s = []
    for i, n in enumerate(a):
        s.append(str(p[i] - n))
    print(" ".join(s))
