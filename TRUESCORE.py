# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if c>=a and d>=b:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

