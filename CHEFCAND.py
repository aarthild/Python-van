# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=a-b
    if a>b:
        print(math.ceil(c/4))
    else:
        print(0)
