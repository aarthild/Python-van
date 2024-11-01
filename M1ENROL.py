# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if b-a>=0:
        print(b-a)
    else:
        print(0)
