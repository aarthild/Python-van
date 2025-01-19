# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    if 2 * n >= k * (k + 1):
        print("YES")
    else:
        print("NO")