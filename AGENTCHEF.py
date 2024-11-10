# cook your dish here
import math
x=int(input())
for _ in range(x):
    a=int(input())
    b=float((20*a)/100)
    c=float(100/b)
    print(math.ceil(c))
