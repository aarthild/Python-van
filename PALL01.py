# cook your dish here
def palin(x):
    temp=x 
    rev=0
    while x>0:
        rem=x%10
        rev=rev*10+rem
        x=x//10
    if temp==rev:
        print("wins")
    else:
        print("loses")
x=int(input())
for _ in range(x):
    a=int(input())
    palin(a)
    
