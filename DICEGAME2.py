# cook your dish here
x=int(input())
for _ in range(x):
    a,b,c,d,e,f=map(int,input().split())
    m=[a,b,c]
    m.sort()
    n=[d,e,f]
    n.sort()
    if m[1]+m[2]>n[1]+n[2]:
        print("alice")
    elif m[1]+m[2]==n[1]+n[2]:
        print("tie")
    else:
        print("bob")
    
