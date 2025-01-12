def prize(n,a,b,c):
    if n<10: return 0
    elif n<21: return a 
    elif n<42: return b 
    else: return c 

for i in range(int(input())):
    D,d,a,b,c = map(int,input().split())
    dis = D*d
    ans = prize(dis,a,b,c)
    print(ans)