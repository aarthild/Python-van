# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    s=sum(c)
    e=a*b
    print(max(0,e-s))
