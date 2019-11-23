
import fileinput

a = [c for c in [line.split() for line in fileinput.input()]]
for l in a:
    for i, n in enumerate(l):
        l[i] = int(l[i])

if ((a[0][0] + a[0][1])/2 + (a[0][2] + a[0][3])/2) > ((a[1][0] + a[1][1])/2 + (a[1][2] + a[1][3])/2):
    print('Gunnar')
elif ((a[0][0] + a[0][1])/2 + (a[0][2] + a[0][3])/2) < ((a[1][0] + a[1][1])/2 + (a[1][2] + a[1][3])/2):
    print('Emma')
else:
    print('Tie')
