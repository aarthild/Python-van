# cook your dish here
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=[]
    p=0
    for i in range(len(b)):
        if b[i]>=p:
            c.append(1)
            p=b[i]
        else:
            c.append(0)
    print(*c)