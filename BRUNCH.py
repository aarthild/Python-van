# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if a//b<=20:
        print(a//b)
    else:
        print(20)
