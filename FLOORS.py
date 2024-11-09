# cook your dish here
import math
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    c=math.ceil(a/10)
    d=math.ceil(b/10)
    if d-c>=0:
        print(d-c)
    else:
        print((d-c)*-1)
