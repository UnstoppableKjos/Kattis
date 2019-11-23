
import fileinput

string = [line for line in fileinput.input()]
string = [c for c in string[0]]

result = string[0]

for i, c in enumerate(string):
    if c == '-':
        result += string[i+1]
print(result)
