for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    flag=0 # 0 vala short , 1 vala long
    for i in a:
        if i<=d:
            if flag!=0:
                c+=1
            flag=0
        else:
            if flag!=1:
                c+=1
            flag=1
    print(c)
    
        
