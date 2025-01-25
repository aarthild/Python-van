# cook your dish here

for i in range(int(input())):

    n,x=map(int,input().split())
    if x>(2*n)-x:
        print(2*(x-n))
    elif x<=(2*n)-x:
        print(0)