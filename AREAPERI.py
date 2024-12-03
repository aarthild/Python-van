a=int(input())
b=int(input())
are=a*b 
per=2*(a+b)
if are>per:
    print("Area")
    print(are)
elif are==per:
    print("Eq")
    print(per)
else:
    print('Peri')
    print(per)
