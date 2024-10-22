# cook your dish here
x=int(input())
for j in range(x):
    a,b,c=map(int,input().split())
    if (b*1+c*2)>=a:
        print("qualify")
    else:
        print("notqualify")