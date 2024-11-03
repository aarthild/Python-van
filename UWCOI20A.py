# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    b=list(map(int,input().split()))
    c=set(b)
    print(max(c))
