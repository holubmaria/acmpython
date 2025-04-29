#Realtional Operators
from sys import stdin

n = int(input())
for i in range(n):
    tokens = input().split()
    a = int(tokens[0])
    b = int(tokens[1])
    if (a < b):
        print("<")
    elif (a > b):
        print(">")
    elif(a == b):
        print("=")