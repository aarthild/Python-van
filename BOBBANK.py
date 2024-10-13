# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    y=b-c
    print(a+(y*d))