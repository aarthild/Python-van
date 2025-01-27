for _ in range(int(input())):

    n=int(input())

    a=list(map(int,input().split()))
    tot=int((n+1)*100*0.5)
    arr_sum=sum(a)
    req=tot-arr_sum
    if req>100:
        print(-1)
    else:
        print(max(0,req))
