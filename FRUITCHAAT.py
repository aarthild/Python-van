# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if b>=a//2:
        print(a//2)
    else:
        print(b)
