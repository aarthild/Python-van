# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        print("yes")
    else:
        print("No")
        
    
        
