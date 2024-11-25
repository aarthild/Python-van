# cook your dish here
a=int(input())
for i in range(1,a+1):
    b=int(input())
    if b<=3:
        print("bronze")
    elif b>3 and b<=6:
        print("silver")
    else:
        print("gold")
