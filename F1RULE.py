# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=107/100
    if a*c<b:
        print("no")
    else:
        print("yes")
