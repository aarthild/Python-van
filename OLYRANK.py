# cook your dish here
for i in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    g=a+b+c 
    h=d+e+f 
    if g>=h:
        print(1)
    else:
        print(2)
