# cook your dish here
import sys
def solve():
    pass

for _ in range(int(input())):
    a, b, x = map(int, sys.stdin.readline().split())
    if x*x >= a*b:
        print(0)
    elif x*x < min(a, b):
        print(2)
    else:
        print(1)
