# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d=map(int,input().split())
    if a+c>=a+d and a+c>=b+c and a+c>=b+d:
        print(a+c)
    elif a+d>=a+c and a+d>=b+c and a+d>=b+d:
        print(a+d)
    elif b+c>=a+c and b+c>=a+d and b+c>=b+d:
        print(b+c)
    else:
        print(b+d)
        
