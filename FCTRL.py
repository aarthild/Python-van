# cook your dish here
for _ in range(int(input())):
    n=int(input())
    zeros=0
    while(n>=5):
        n=n//5
        zeros+=n 
    print(zeros)
