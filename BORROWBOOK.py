# cook your dish here

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = {}
    for i in range(n):
        d = a[i]
        l = i + 1
        if d in p:
            p[d] = max(p[d], l)
        else:
            p[d] = l
    print(sum(p.values()))
