# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    if a<1500:
        print(float(a+(a*10)/100+(a*90)/100))
    else:
        print(float(a+500+(a*98)/100))
    
