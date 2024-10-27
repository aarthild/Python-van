# cook your dish here
import math
x=int(input())
for i in range(x):
    a=int(input())
    if a>0:
        b=math.ceil(a/3)
        print(b*3-a)
    else:
        print(0)
