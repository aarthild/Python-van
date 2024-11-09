# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    e=a-b
    f=c-d
    g=e+f
    if g<0:
        print("yes")
    else:
        print("No")
