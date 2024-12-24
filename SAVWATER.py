# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    p=b+c//2
    q=p*a
    if(q<=d):
        print("yes")
    else:
        print("no")
    