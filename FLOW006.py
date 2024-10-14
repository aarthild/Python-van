# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    s=0
    while a>0:
        rem=a%10
        s=s+rem
        a=a//10
    print(s)
