# cook your dish here
for i in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
        
    border=y/x
    ans=0
    for i in a:
        if i <= border:
            ans+=(x*i)
        else:
            ans+=y
            
    print(ans)