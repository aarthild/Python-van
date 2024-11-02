# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if b%2!=0:
        print(math.ceil(b/2))
    else:
        print(math.ceil(b/2)+1)
