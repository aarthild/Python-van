# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    d=abs(b-c)
    if a>d:
        print("Yes")
    else:
        print("No")
