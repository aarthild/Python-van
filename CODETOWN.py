# cook your dish here

t=int(input())

for _ in range (t):
    s=input()
    s1="CODETOWN"
    v=["A","E","I","O","U"]
    flag = "YES"
    for i in range (len(s)):
        if(s[i]==s1[i]):
            continue
        elif (s[i] not in v and s1[i] not in v):
            continue
        elif(s[i] in v and s1[i] in v):
            continue
        else:
            flag="NO"
            break
    print(flag)
