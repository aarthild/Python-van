# cook your dish here
x=int(input())
for _ in range(x):
    x,y,z=map(int,input().split())
    if (x*y)%z==0:
        print(x*y,z)
    elif (x*z)%y==0:
        print(x*z,y)
    elif (z*y)%x==0:
        print(z*y,x)
    else:
        print(-1)
    

        
        
