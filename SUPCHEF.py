# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if b*c<a:
        print("Yes")
    else:
        print("No")
