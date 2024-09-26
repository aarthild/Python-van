# cook your dish here
n=int(input())
for i in range(1,n+1):
    x,y,z=map(int,input().split())
    if y-x == z-y:
        print("0")
    else:
        print("1")
