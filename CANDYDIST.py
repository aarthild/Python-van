# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if a%b==0:
        if (a//b)%2!=0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
