# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a*b<=c:
        print("0")
    else:
        d=(a*b)-c
        print(math.ceil(d/b))
