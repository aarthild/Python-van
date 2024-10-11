# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a<b:
        print(a)
    elif a==b:
        print(a)
    else:
        print(b)
