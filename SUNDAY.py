# cook your dish here
t = int(input())
s=[6,13,20,27,7,14,21,28]
for i in range(t):
    count=0
    n = int(input())
    arr=list(map(int,input().split()))
    for j in arr:
        if j not in s:
            count+=1
    print(count+8)
