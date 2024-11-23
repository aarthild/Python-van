# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    e=b*7
    f=(a*c)+(7-a)*d
    print(max(e,f))
