# cook your dish here
for i in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    b=input()
    
    ans=m
    for i in range(n-m+1):
        diff=0
        for j in range(m):
            if b[j] != a[i+j]:
                diff+=1
                
        ans = min(ans,diff)
        
    print(ans)
