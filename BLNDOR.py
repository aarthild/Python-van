# cook your dish here

t=int(input())

for  _ in range(t):
    n=int(input())
    c=0
    f=True
    a=list(map(int,input().split()))
    for i in a:
        if i==2:
            c=c+1
        if c%8==0:
            f=True
        else:
            f=False
    if f==True:
        print("YES")
    elif f==False:
        print("NO")
    
    # for i in a:
    #     p=p*i
    # x=p**(1/8)
    # if x%round(x)==0:
    #     print("YES")
    # else:
    #     print("NO")
    # # print(x)
