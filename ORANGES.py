# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    print('Yes' if k>=n*10 and k<=n*12 else 'No')