# cook your dish here
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    
    even = n // 2
    odd = n - even 
    
    if x % 2 == 0:
        print(even-1)
    else:
        print(odd-1)
        