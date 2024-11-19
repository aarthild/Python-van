x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    e=abs(a-c)
    f=abs(b-d)
    print(max(e,f))
