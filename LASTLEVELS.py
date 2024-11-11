x=int(input())
import math
for _ in range(x):
    a,b,c=map(int,input().split())
    if a<=3:
        print(a*b)
    else:
        d=(math.ceil(a/3))-1
        print(a*b+d*c)

