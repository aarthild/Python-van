# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    e=max(a,b)
    f=max(c,d)
    if e<f:
        print("p")
    elif e==f:
        print("tie")
    else:
        print("q")
