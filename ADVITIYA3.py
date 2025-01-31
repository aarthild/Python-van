PP = int(input())
for _ in range(PP):
    m, l = map(int, input().split())
    t = list(map(int, input().split()))
    
    ans = []
    count = 0
    
    for i in range(m):
        if l <= t[i]:
            q = t[i] % l
            ans.append(q)
            count += 1
    
    if count < 1:
        print("-1")
    else:
        ans.sort()
        print(ans[0])

 
