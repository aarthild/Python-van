# cook your dish here
import math
x=int(input())
for _ in range(x):
    c=0
    n=0
    a=int(input())
    if a>=4:
        print(math.ceil(a/4))
    else:
        print(1)
    