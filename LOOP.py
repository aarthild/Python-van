# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    e=c-d
    print(min(d,e))
