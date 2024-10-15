l=list(map(int,input().split()))
def merge(l,start,mid,end):
    left=l[start:mid+1]
    right=l[mid+1:end+1]
    i=0
    ans=[]
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i=i+1
        else:
            ans.append(right[j])
            j=j+1
    while i<len(left):
        ans.append(left[i])
        i=i+1
    while j<len(right[j]):
        ans.append(right[j])
        j=j+1
    l[start:end+1]=ans[:]
def divide(l,start,end):
    mid=(start+end)//2
    if start<end:
        divide(l,start,mid)
        divide(l,mid+1,end)
        merge(l,start,mid,end)
    
