# cook your dish here
x=int(input())
for i in range(x):
    a=list(map(int,input().split()))
    print(max(a)-min(a))
    
