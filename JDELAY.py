# cook your dish here
T=int(input())

for i in range(T):
    c=0
    n=int(input())
    for j in range(n):
        x,y=map(int, input().split())
        z=y-x
        if(z>5):
            c+=1
    print(c)
