# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=a//(b+1)
    print(a-b*c)
