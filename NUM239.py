# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if i%10==2 or i%10==3 or i%10==9:
            c+=1 
    print(c)
