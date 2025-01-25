# cook your dish here

for i in range(int(input())):

    n,l,x=map(int,input().split())
    if l<(n-l):
        print(x*l)
    elif l>(n-l):
        print((n-l)*x)
    elif l==(n-l):
        print(x*l)
