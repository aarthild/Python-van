# cook your dish here
import math
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    c=abs(b-a)
    print(math.ceil(c/2))
