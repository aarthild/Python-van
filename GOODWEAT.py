# cook your dish here
x=int(input())
for _ in range(x):
    a=list(map(int,input().split()))
    b=a.count(0)
    c=a.count(1)
    if b>c:
        print("No")
    else:
        print('yes')
