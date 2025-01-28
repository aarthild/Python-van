# cook your dish here

t = int(input())


for _ in range(t):
    s = int(input())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(s - 1):
        max_sum = max(max_sum, a[i] + a[i + 1])
        max_sum = max(max_sum, a[0] + a[-1])  
    print(max_sum)
