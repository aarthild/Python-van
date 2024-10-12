# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a>=30*b:
        print("YES")
    else:
        print("NO")
