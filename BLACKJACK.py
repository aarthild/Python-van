# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    for i in range(1,11):
        c=1
        if a+b+c*i==21:
            print(i)
            break
    else:
            print(-1)