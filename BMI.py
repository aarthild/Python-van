# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=a//(b**2)
    if c<=18:
        print('1')
    elif c>18 and c<=24:
        print('2')
    elif c>24 and c<=29:
        print('3')
    else:
        print('4')
        
