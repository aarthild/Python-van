# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if a*10>=b:
        print(b*c)
    else:
        print(a*10*c)
