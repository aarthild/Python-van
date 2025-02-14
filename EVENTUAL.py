# cook your dish here

t=int(input())

for i in range(t):
    n=int(input())
    s=input()
    l=list(s)
    s1=set(l)
    c=0
    for i in s1:
        if l.count(i)%2!=0:
            print("NO")
            break
        else:
            c+=1
    if(c==len(s1)):
        print("YES")
   
