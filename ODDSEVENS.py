
# cook your dish here
for i in range(int(input())):
    a=list(map(int,input().split()))
    b=sum(a)
    if b%2==0:
        print('bob')
    else:
        print("alice")
