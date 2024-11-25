# cook your dish here
def factorial(n): 
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n - 1)) 
a=int(input())
for i in range(1,a+1):
    b=int(input())
    print(factorial(b))
