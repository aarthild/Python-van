import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    # print(math.ceil(n/2))
    if math.ceil(n/2) == k or math.ceil(n/2) == k+1:
        print("yes")
    else:
        print("no")
