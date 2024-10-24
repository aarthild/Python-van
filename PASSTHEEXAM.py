# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a+b+c>=100 and a>=10 and b>=10 and c>=10:
        print("Pass")
    else:
        print("fail")
