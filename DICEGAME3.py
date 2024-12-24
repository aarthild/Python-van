# cook your dish here
for i in range(int(input())):
    n=int(input())
    print(((n//2)*12+(n//2)*1+6) if(n%2!=0) else ((n//2)*12+(n//2)*1))