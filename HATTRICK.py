# cook your dish here
x=int(input())
for _ in range(x):
    a=list(map(str,input().split()))
    for i in range(4):
        if a[i]==a[i+1]==a[i+2]=='W':
            print("yes")
            break 
    else:
        print('no')
