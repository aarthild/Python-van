# cook your dish here
for i in range(int(input())):
    a,b,c,m=map(int,input().split())
    mins=min(abs(a-b),abs(a-c),abs(b-c))
    if mins<=m:
        print("yes")
    else:
        print("No")