# cook your dish here
for i in range(int(input())):
    n = int(input())
    arrs = list(map(int,input().split()))
    arrd = list(map(int,input().split()))
    e = 0
    for i in range(n):
        if arrs[i]==arrd[i]:
            e+=1
    print(e)