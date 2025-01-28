# cook your dish here
t=int(input())
for _ in range(t):
    n,x,y,a,b=map(int,input().split())
    petrol_mileage=a/x
    diesel_mileage=b/y 
    if petrol_mileage>diesel_mileage:
        print("PETROL")
    elif diesel_mileage>petrol_mileage:
        print('DIESEL')
    else:
        print("ANY")