# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    if (a/b)<(c/d):
        print("Bob")
    elif (a/b)==(c/d):
        print("equal")
    else:
        print("alice")
