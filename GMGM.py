# cook your dish here

J = int(input())


for _ in range(J):
    N,D = map(int,input().split())
    B = list(map(int, input().split()))
    
    switches = 0
    holding_close_range_gun = True
    for i in range(N):
        if holding_close_range_gun and B[i] > D:
             switches += 1
             holding_close_range_gun = False
        elif not holding_close_range_gun and B[i] <= D:
            switches += 1
            holding_close_range_gun = True
    print(switches)        