# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if c%a==0 and c%b==0:
        print("any")
    elif c%b==0:
        print("duck")
    elif c%a==0:
        print("chicken")
    else:
        print("none")