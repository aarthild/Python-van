# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    d=a[1]+a[3]+a[5]+a[7]+a[9]
    c=a[0]+a[2]+a[4]+a[6]+a[8]
    if(c==d):
        print("0")
    elif(c>d):
        print("1")
    else:
        print("2")
