# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if b<=a:
        print(0)
    else:
        c=b-a
        print(math.ceil(c/8))
