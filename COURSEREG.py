# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if b>=a+c:
        print("yes")
    else:
        print("no")