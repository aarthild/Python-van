# cook your dish here
for _ in range(int(input())):
    z,y,a,b,c=map(int,input().split())
    if z>=(y+a+b+c):
        print('yes')
    else:
        print('no')
