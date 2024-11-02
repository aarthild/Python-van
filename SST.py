# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if 10*a>5*b:
        print("FIRST")
    elif 10*a==5*b:
        print("ANY")
    else:
        print("SECOND")
    
