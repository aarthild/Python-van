# cook your dish here
n=int(input())
c=0
s=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]%2==0:
        c+=1
    else:
        s+=1
if c>s:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
