# cook your dish here
import math
for i in range(int(input())):
    n,m=map(int,input().split())
    print(math.lcm(n,m)//math.gcd(n,m))