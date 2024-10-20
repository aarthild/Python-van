# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a<50:
        print("Z")
    elif b<50 and a>=50:
        print("F")
    else:
        print("A")