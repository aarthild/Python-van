# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if b*c>=a:
        print("yes")
    else:
        print("no")
