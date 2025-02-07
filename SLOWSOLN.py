# cook your dish here

for i in range(int(input())):

    a,b,c=map(int, input().split())
    #s=0
    '''for j in range(a):
        if(s<c):
            s=s+b
        else:
            break
    if(s!=c):
        s-=b 
    print(s)'''
    if(a*b<=c):
        q=0
        while(a>0):
            q=q+b**2
            a-=1
        print(q)
    else:
        q1=0
        if(c%b==0):
            w=c//b
            while(w>0):
                q1=q1+b**2
                w-=1 
            print(q1)
        else:
            q2=0
            w1=c//b
            while(w1>0):
                q2=q2+b**2
                w1-=1
            q2=q2+(c%b)**2 
            print(q2)