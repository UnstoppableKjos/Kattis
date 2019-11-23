
import fileinput

x, y = [int(line.rstrip()) for line in fileinput.input()]

if x > 0 and y > 0:
    print(1)
elif y > 0 > x:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 > y:
    print(4)
