# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if abs(a-b)<=c:
        print("Yes")
    else:
        print('No')
