for _ in range(int(input())):
    n=int(input())
    b=input()
    a=list(b)
    count1=0
    count2=0
    if a[0]=='A':
        count1+=1
    for i in range(0,n-1):
        if a[i]==a[i+1] and a[i]=='A':
            count1+=1
        elif a[i]==a[i+1] and a[i]=='B':
            count2+=1
    print(count1,count2)