# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    if a%10==0:
        print(100-a)
    else:
        b=100-a
        print(b-(b%10))
        
        
