# cook your dish here
n=int(input())
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("YES")
    else:
        print("NO")
