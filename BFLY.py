# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a+b<c or a+c<b or b+c<a:
        print("nO")
    else:
        print('yes')