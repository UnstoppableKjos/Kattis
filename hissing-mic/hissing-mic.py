
import fileinput

for line in fileinput.input():
    w = [c for c in line.rstrip()]
    hiss = False
    for i, c in enumerate(w):
        if i > 0:
            if c == 's' and w[i-1] == 's':
                hiss = True
    if hiss:
        print("hiss")
    else:
        print("no hiss")
