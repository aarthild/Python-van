# cook your dish here
for _ in range(int(input())):
    n,x,d=map(int,input().split())
    v=n//(x*5)
    print(v+d)