# cook your dish here
t=int(input())
while t!=0:
    x,y=map(int,input().split())
    if(x**4 + 4*(y**2))==(4*x**2 * y):
        print("YES")
    else:
        print("NO")
    t-=1
