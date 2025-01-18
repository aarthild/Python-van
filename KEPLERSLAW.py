# cook your dish here
for i in range(int(input())):
    a,r,t,i=map(int,input().split())
    if a**2/t**3==r**2/i**3:
        print("yes")
    else:
        print('No')
