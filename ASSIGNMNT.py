# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if a*b<=c*60*24:
        print("YES")
    else:
        print("No")
        
