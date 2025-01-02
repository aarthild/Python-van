# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if 2*max(a,b,c)<=a+b+c+1:
        print('yes')
    else:
        print('no')