# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a*b<=c:
        print("yes")
    else:
        print("no")