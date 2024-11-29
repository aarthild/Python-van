# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    if c/a < d/b:
        print("-1")
    elif c/a == d/b:
        print('0')
    else:
        print("1")
