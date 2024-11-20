# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    b=0
    while a>0:
        c=a%2
        b=b+c
        a=a//2
    if b%2==0:
        print("even")
    else:
        print("Odd")