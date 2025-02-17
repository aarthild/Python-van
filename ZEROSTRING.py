# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=str(input())
    a=0
    b=0
    for i in range(n):
        if(s[i]=="0"):
            a+=1
        else:
            b+=1
    if(a>=b):
        print(b)
    else:
        print(a+1)
