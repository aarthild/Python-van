t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    k=[]
    s = sum(a)
    p=0
    for i in range(n):
        p = s - a[i]
        k.append(p)
    maxi = max(k)
    print(maxi)
        # cook your dish here
