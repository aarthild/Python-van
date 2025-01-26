# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    s=sum(c)
    print(math.ceil(s/b))