# cook your dish here

from collections import Counter

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))[:n]
    c=Counter(l)
    m=max(c,key=c.get)
    #print(m)
    print(n-l.count(m))
