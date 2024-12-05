# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a%2==b%2:
        print("yes")
    else:
        print('no')