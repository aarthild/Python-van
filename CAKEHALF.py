# cook your dish here
t = int(input())
for i in range(0,t):
    A, B = map(int, input().split())
    count = 0
        
    if A == B:
        print("0")
    else:
        while A != B:
            if A > B:
                count += (A + 1) // 2
                A -= (A + 1) // 2
            else:
                count += (B + 1) // 2
                B -= (B + 1) // 2
        print(count)