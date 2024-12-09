# cook your dish here
# cook your dish here
for i in range(int(input())):
    a = list(map(str,input().split()))
    b = list(map(str,input().split()))
    for i,n in enumerate(a):
        if n in b:
            print(n)
            break
