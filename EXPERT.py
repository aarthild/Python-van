# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    m=math.ceil(a/2)
    if b>=m or a==b:
        print("YES")
    else:
        print("NO")
