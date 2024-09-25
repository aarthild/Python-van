# cook your dish here
n=int(input())
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    if b+(2*c)<=a:
        print("YES")
    else:
        print("no")
