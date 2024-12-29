# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    # a=n*(2**m)
    # b=((n+1000)*m)
    if x<1000:
        x=x+1000
        if y>1:
            x=x*(2**(y-1))
    else:
        x=(x*(2**y))
    print(x)