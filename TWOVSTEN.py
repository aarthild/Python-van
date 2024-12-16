# cook your dish here
for i in range(int(input())):
    x=int(input())
    if x%5==0 and x%10==0:
        print(0)
    elif x%5==0 and x%10!=0:
        print(1)
    elif x%5!=0:
        print(-1)
    
