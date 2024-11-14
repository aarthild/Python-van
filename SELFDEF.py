# cook your dish here 
x=int(input())
for _ in range(x):
    c=0
    a=int(input())
    b=list(map(int,input().split()[:a]))
    for i in range(len(b)):
        if b[i]>=10 and b[i]<=60:
            c=c+1
    print(c)
