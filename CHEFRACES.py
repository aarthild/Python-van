# cook your dish here
t=int(input())

for i in range(t):

    x,y,a,b=map(int,input().split())
    if (x==a or x==b) and (y==b or y==a):
        print("0")
    elif (x==a or x==b) or (y==b or y==a):
        print("1")
    else:
        print("2")
