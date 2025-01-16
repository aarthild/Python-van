# cook your dish here
for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    s=0
    for i in range(3):
        if a[i]>=b[i]:
            c+=1
        else:
            s+=1
    if c>=s:
        print("A")
    else:
        print("B")
            
