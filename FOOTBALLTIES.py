# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    m=min(x,y)%3
    print(m)