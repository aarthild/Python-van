# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if m < n:
        print(n - m)
    else:
        print(min(m % n, (-m) % n))