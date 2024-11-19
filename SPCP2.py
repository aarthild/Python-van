# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if (a*100-b)>=0:
        print(0)
    else:
        print(math.ceil(abs(a*100-b)/100))