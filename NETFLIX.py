# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a+b>=d or b+c>=d or a+c>=d:
        print("yes")
    else:
        print("no")
