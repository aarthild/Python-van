# cook your dish here
x,y,k=map(int,input().split())
a=(x-y)
if (x-y)>=0:
    a=x-y
else:
    a=(x-y)*-1
if a<=k:
    print("YES")
else:
    print("NO")