# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    d=a*b
    print(math.ceil(d/4))
