# cook your dish here
t=int(input())
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]

for _ in range(t):
    n=int(input())
    c=0 
    for i in range(len(l)-1,-1,-1):
        if n==0:
            break 
        if n>=l[i]:
            r=int(n/l[i])
            c+=r  
            n-=r*l[i]
    print(c)
