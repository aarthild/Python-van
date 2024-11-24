# cook your dish here
x=int(input())
for _ in range(x):
    n=int(input())
    c=0
    for x in [100,50,10,5,2,1]:
        y=n//x
        n-=y*x
        c+=y
    print(c)
    