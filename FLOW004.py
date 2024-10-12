# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    rem=a%10
    c=str(a)
    n=a/pow(10,len(c)-1)
    print(int(n+rem))