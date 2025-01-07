# cook your dish here
for i in range(int(input())):
    b=int(input())
    c=0
    while b!=2:
        b-=2
        if b<2:
            break
        c+=1
    s=0
    for i in range(1, c+1):
        s+=i
    print(s)
