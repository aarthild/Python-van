# cook your dish here
x=int(input())
for _ in range(x):
    l=list(map(int,input().split()))
    e=0
    o=0
    for i in range(len(l)):
        if l[i]==1:
            o=o+1 
        else:
            e=e+1
    if o>=1:
        print("OUT")
    else:
        print("IN")
