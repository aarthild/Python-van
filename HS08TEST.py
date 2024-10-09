# cook your dish here
a,b=map(float,input().split())
f=a+0.50
if a%5==0 and b>=f:
    print(b-f)
else:
    print(b)
    
