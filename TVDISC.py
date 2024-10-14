# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a-c < b-d:
        print("first")
    elif a-c==b-d:
        print("any")
    else:
        print("second")