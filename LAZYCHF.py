# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    print(min(a*b,a+c))
