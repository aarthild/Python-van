# cook your dish 
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    a,b=map(int,input().split())
    for num in range(a,b+1):
        if prime(num):
            print(num)
