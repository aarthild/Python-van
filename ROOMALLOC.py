# cook your dish here
import math
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in range(n):
        k=math.ceil(a[j]/2)
        c+=k
    print(c)