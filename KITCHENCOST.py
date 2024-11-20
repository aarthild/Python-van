t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here.
    s=0
    for i in range(n):
        if a[i]>=x:
            s=s+b[i]
    print(s)
            
    t -= 1
