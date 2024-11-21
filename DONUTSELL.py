# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    c=list(map(int,input().split()[:a]))
    d=list(map(int,input().split()[:b]))
    e=0
    for i in range(b):
        if c[d[i]-1] >0:
            c[d[i]-1]-=1
        else:
            e=e+1
    print(e)
    
