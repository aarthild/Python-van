# cook your dish here
x=int(input())
for i in range(1,x+1):
    a,b=map(int,input().split())
    if a>b:
        print("new phone")
    elif a==b:
        print("any")
    else:
        print("repair")