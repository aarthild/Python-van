# cook your dish here
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a-b>=0:
        print(a-b)
    else:
        print("0")