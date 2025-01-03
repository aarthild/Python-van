# cook your dish here
for i in range(int(input())):
    n,x,y=map(int,input().split())
    o=n*x 
    if n%2==0:
        m=(n//2)*y
    else:
        m=(n//2)*y+x 
    print(max(o,m))
