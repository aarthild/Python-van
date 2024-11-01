# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print("ALICE")
    elif b>a and b>c:
        print("BOB")
    else:
        print("CHARLIE")
