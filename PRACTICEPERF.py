# cook your dish here
l=list(map(int,input().split()))
n=len(l)
c=0
for i in range(0,n):
    if l[i]>=10:
        c+=1
print(c)
    

