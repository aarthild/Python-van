# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b>c:
        print('train')
    elif a+b==c:
        print('equal')
    else:
        print('planebus')
