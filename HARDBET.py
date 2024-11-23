# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    d=min(a,b,c)
    if a==d:
        print("Draw")
    elif b==d:
        print("Bob")
    else:
        print("alice")
