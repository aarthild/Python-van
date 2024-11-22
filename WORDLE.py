# cook your dish here
x=int(input())
for _ in range(x):
    a=list(input())
    b=list(input())
    ans=" "
    for i in range(len(a)):
        if a[i]==b[i]:
            ans+="G" 
        else:
            ans+="B" 
    print(ans)
    ans=" "
