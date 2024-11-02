# cook your dish here
x=int(input())
for _ in range(x):
    s=0
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=len(c)
    for i in range(d):
        if c[i]>=b:
            s+=1
    print(s)
    