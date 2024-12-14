# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    c=[]
    for i in p:
        if i>k:
            c.append(k)
        else:
            c.append(i)
    print(sum(p)-sum(c))
