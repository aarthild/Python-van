# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if c%b==0:
        print("YES")
    else:
        print("NO")
