# cook your dish here
for i in range(int(input())):
    n,k,p = map(int,input().split())
    a = list(map(int,input().split()))
    #this chair is given to Ved
    maxa = max(a)
    if sum(a) - maxa + p > k + maxa:
        print("Varun")
    elif sum(a) - maxa + p < k + maxa:
        print("Ved")
    else:
        print("Equal")