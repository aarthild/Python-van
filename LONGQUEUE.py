# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        k=a[i]/2
        if(k>=a[i-1]):
            a[i-1]=a[i]
        elif(k<a[i-1]):
            print(i+1)
            break
        
        