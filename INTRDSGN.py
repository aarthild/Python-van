# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a+b>c+d:
        print(c+d)
    else:
        print(a+b)