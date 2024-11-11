# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    if a!=c:
        if a+c==180:
            print("Yes")
        else:
            print("no")
    else:
        if b+d==180:
            print("Yes")
        else:
            print("No")
        
