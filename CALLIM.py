# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    c=list(map(int,input().split()[:a]))
    d=0
    e=0
    for i in c:
        if i+e<=b:
            e+=i
            d+=1
        else:
            break
    print(d)
        
    
