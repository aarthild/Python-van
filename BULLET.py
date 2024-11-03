# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    d=b//a
    if c-d>0:
        print(c-d)
    else:
        print(0)
    
