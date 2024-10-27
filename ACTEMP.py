# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if max(a,c)<=b:
        print("YES")
    else:
        print("NO")
