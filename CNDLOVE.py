# cook your dish here

for i in range(int(input())):

    x=int(input())
    l=list(map(int,input().split()))
    if(sum(l)%2==1):
        print('YES')
    else:
        print('NO')