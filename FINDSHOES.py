# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    print(max(0,a-b)+a)