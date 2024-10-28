
# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=a*100//100
    d=b*200//100
    if 100-c>200-d:
        print("SECOND")
    elif 100-c==200-d:
        print("BOTH")
    else:
        print("FIRST")