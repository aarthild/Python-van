# cook your dish here
for i in range(int(input())):
    n,x,k=map(int,input().split())
    a=x%k
    b=(n-x)%k
    print((a+b)-(2*(min(a,b))))
