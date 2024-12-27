t = int(input())
for _ in range(t):
    h, l, w = map(int, input().split())
    print(1000 // (2 * (h * l + l * w + h * w)))
