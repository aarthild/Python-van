# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    c=(a//b)
    s=0
    while c>0:
        s+=1
        c=c//b
    print(s+1)
