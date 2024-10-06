# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    m=b-c
    print(m*a)