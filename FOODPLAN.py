# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    a=a-a/10
    if(a<b):
        print("ONLINE")
    elif (a==b):
        print("EITHER")
    else:
        print("DINING")