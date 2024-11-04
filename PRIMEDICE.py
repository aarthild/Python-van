# cook your dish here
x=int(input())
for _ in range(x):
    s=0
    a,b=map(int,input().split())
    c=a+b 
    for i in range(1,c+1):
       if c%i==0:
            s+=1
    if s==2:
        print("Alice")
    else:
        print("Bob")
    
        
