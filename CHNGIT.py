# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a.count(a[i]))
    maxm= max(b)
    print(n-maxm)