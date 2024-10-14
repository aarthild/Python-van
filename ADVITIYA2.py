# cook your dish here
x=int(input())
for _ in range(x):
    a=list(map(int,input().split()))
    count=0
    for m in a:
        if m==1:
            count+=1
    if count>=4:
        print("yes")
    else:
        print("no")