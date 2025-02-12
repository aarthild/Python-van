for i in range(int(input())):

    n=int(input())

    s=list(input())
    s1=''
    if len(s)%2==0:
        for i in range(0,n,2):
            (s[i],s[i+1])=(s[i+1],s[i])
    else:
        for i in range(0,n-1,2):
            (s[i],s[i+1])=(s[i+1],s[i])
    for ele in s:
        if ele=='z':
            ele=chr(ord('a'))
            s1+=ele
        else:
            ele=chr(ord('a')+(ord('z')-ord(ele)))
            s1+=ele
    print(s1)
