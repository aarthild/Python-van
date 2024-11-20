# cook your dish 
import math
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    d=math.ceil(b/c)
    print(a*(d))
