# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    b=a%4
    if b>=2:
        print("yes")
    else:
        print("No")
