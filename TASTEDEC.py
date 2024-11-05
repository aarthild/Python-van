# cook your dish here
x=int(input())
for i in range(1,x+1):
    a,b=map(int,input().split())
    if 2*a>5*b:
        print("chocolate")
    elif 2*a==5*b:
        print("either")
    else:
        print("candy")
