# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    print(max(a,b,c))