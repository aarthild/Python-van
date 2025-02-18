# cook your dish here

t=int(input())

while(t>0):
    n=int(input())
    p=list(map(int,input().split()))
    if(p[0]==1 and p[n-1]==n):
        print(0)
    else:
        count=0
        for i in range(0,n):
            if(p[i]==n):
                for j in range(i+1,n):
                    if(p[i]>p[j]):
                        p[i],p[j]=p[j],p[i]
                        count+=1
                    break
        for i in range(0,n):
            if(p[i]==1):
                for j in range(i-1,-1,-1):
                    if(p[i]<p[j]):
                        p[i],p[j]=p[j],p[i]
                        i=j
                        count+=1
                break
        print(count)
    t-=1
    