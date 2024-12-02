# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0:
        print("liquid")
    elif b==0:
        print('solid')
    else:
        print('solution')
