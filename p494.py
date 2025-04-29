from sys import stdin
for line in stdin:
    l = line.replace(".", "")
    words = len(l.split())
    print(words)