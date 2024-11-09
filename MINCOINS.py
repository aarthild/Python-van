# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    if a%10==0:
        print(a//10)
    elif a%5==0:
        print((a//10)+1)
    else:
        print("-1")
