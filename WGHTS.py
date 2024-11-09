# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    if b+c==a or c+d==a or b+d==a or a==b or a==c or a==d or a==b+c+d:
        print("Yes")
    else:
        print("No")
    
