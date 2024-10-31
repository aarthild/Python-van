# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if a==0 and b==0:
        print(7)
    elif a<b:
        print(7-b)
    else:
        print(7-a)
    