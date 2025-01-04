# cook your dish here
# cook your dish here
t = int(input())

for _ in range(t):
    s= -1
    m= -1
    
    for i in range(22):
        r, w= map(int, input().split())
        sc = r+(w*20)
        if sc>s:
            s=sc
            m=i+1
            
    print(m)
    
    
    
    