# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    c=0
    b=list(map(int,input().split()))
    for i in range(0,len(b)):
        if b[i]<=4:
            c+=1
            i+=1
    if c>=1:
        print("No")
    else:
        print("yes")
            
