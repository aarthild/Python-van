# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    d=b*3
    e=(a-b)*-1
    if d+e>=c:
        print("Pass")
    else:
        print("fail")
