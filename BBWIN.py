# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    if a>=10+b:
        print("0")
    else:
        while a<10+b:
            a=a+3
            c+=1 
        print(c)
        