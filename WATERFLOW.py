# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a+c*d>b:
        print("overflow")
    elif a+c*d==b:
        print("filled")
    else:
        print("Unfilled")
