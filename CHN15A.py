# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    c=list(map(int,input().split()[:a]))
    d=0
    for i in range(len(c)):
        e=c[i]+b
        if e%7==0:
            d+=1
    print(d)
        