
import fileinput

def isVowel(c):
    if c in ['a', 'e', 'i', 'o', 'u', 'y']:
        return True
    else:
        return False


a = []
for line in fileinput.input():
    a.append(line.rstrip())

while len(a) > 0:
    n = int(a[0])
    maxcnt = 0
    word = ""
    for i in range(1, n+1):
        cnt = 0
        for j, c in enumerate(a[i]):
            if j > 0:
                if isVowel(c) and a[i][j-1] == c:
                    cnt += 1
        if cnt > maxcnt:
            maxcnt = cnt
            word = a[i]
    if len(word) > 0:
        print(word)
    a = a[n+1:]
