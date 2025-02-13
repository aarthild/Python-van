# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(max(a,b)>=2*min(a,b)):
        print('0')
    else:
        if(2*min(a,b)-max(a,b)>(min(a,b)-(max(a,b)//2))):
            print(min(a,b)-(max(a,b)//2))
        else:
            print(2*min(a,b)-max(a,b))
