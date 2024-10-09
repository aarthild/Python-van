# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    p=a*10
    q=a-b
    print((p//100+a)-q)
