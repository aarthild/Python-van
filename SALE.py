# cook your dish here
x=int(input())
for _ in range(x):
    a=list(map(int,input().split()))
    a.sort()
    print(a[1]+a[2])
