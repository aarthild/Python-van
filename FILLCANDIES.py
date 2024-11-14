# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    print(math.ceil(a/(b*c)))
