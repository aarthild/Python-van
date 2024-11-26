# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif a>b:
        if (a - b) % 2 == 0:
            print((a - b) // 2)
        else:
            print((a - b) // 2 + 2)
    else:
        print(b-a)
        
        