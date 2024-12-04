# cook your dish here
x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if (b-a)%3!=2:
        print('yes')
    else:
        print('no')
        
    
