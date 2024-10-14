t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    if a!=b and b!=c and c!=a:
        print("YES")
    else:
        print("NO")
    t -= 1
