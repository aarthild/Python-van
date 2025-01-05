# cook your dish here
import math
for i in range(int(input())):
    d=0
    a=int(input())
    b=list(map(int,input().split()))
    c=math.prod(b)
    if c>=0:
        print("0")
    else:
        print('1')
    
