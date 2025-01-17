# cook your dish here
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    s=0
    c=list(map(int,input().split()))
    p=0
    for i in range(a):
        if b[i]-p>=c[i]:
            s+=1
        p=b[i]
    print(s)
    
    
