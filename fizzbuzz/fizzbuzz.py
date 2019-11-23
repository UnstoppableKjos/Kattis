
import fileinput

for line in fileinput.input():
    x, y, n = line.split()
    x = int(x)
    y = int(y)
    n = int(n)
    for i in range(1, n+1):
        ans = ""
        if i % x == 0:
            ans += "fizz"
        if i % y == 0:
            ans += "buzz"
        if i % x != 0 and i % y != 0:
            ans = i
        print(ans)
