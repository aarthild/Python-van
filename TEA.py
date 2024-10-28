# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    d=math.ceil(a/b)
    print(d*c)
