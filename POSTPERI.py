# cook your dish here
tc=int(input())
for i in range(tc):
    x,y,z=map(int,input().split())
    if 2*(x+y)<=z:
        print(z-2*(x+y))
    elif z<=4:
        print(4-z)
    elif z & 1:
        print(1)
    else:
        print(0)
        
