# cook your dish here
import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print(0)
    else:
        c=math.ceil((10*(b-a))/(100-b))
        print(c)