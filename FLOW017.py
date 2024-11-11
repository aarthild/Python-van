# cook your dish here
x=int(input())
for _ in range(x):
    a=list(map(int,input().split()[:x]))
    a.sort()
    b=len(a)
    print(a[b-2])
    
    
