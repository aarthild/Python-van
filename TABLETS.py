# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if 3*a<=b:
        print("YES")
    else:
        print("NO")