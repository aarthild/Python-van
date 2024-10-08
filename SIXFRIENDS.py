# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if 3*a<=2*b:
        print(3*a)
    else:
        print(2*b)
