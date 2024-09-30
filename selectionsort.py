#l=list(map(int,input().split()))
#for i in range(len(l)):
 #   for j in range(i,len(l)):
   #     if l[i]>l[j]:
   #         l[i],l[j]=l[j],l[i]
#print(l)
l=list(map(int,input().split()))
for i in range(len(l)):
    minimum=l[i]
    index=i
    for j in range(i,len(l)):
        if minimum>l[j]:
            index=j
            minimum=l[j]
    l[i],l[index]=l[index],l[i]
print(l)
