# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a+b<=c:
        print(2)
    elif a<=c:
        print(1)
    else:
        print(0)
