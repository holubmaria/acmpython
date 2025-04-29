from sys import stdin

for line in stdin:
    tokens = line.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(abs(b-a))