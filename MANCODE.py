def max_min(N):
    num_max = (N+1)//2
    num_min = (N+2)//3
    return [num_max, num_min]


for T in range(int(input())):
    
    N = int(input())
    print(*max_min(N))
    
    
