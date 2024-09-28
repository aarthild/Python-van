# cook your dish here
n=int(input())
for i in range(1,n+1):
    x,k=map(int,input().split())
    if (x+k)%2==0:
        print("YES")
    else:
        print("NO")
    