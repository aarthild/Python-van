# cook your dish here
a=int(input())
for i in range(a):
    a,b=map(int,input().split())
    c=max(a,b)
    d=min(a,b)
    e=c-d-1
    print((a+b)+e)
    
    