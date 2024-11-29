# cook your dish here
x=int(input())
a=[]
for i in range(1,11):
    if x%i==0:
        a.append(i)
print(max(a))
