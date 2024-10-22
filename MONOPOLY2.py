# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a>b+c+d or b>a+c+d or c>a+b+d or d>a+b+c:
        print("yes")
    else:
        print("no")
    
