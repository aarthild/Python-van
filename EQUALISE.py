# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    while a<b:
        a=a*2
    print('yes' if a==b else "no")