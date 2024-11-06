# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=a+b 
    if (c//2)%2==0:
        print("ALice")
    else:
        print("BOB")