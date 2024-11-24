# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if a+c*2>=b:
        print("yes")
    else:
        print("No")
