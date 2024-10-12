# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if a+b==c or b+c==a or a+c==b:
        print("YES")
    else:
        print("No")