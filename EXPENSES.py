# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    print(2**(b-a))