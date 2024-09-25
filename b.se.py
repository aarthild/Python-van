l = list(map(int,input().split()))
l.sort()
key = l[2]
low = 0
high = len(l)-1
c=0
while low <= high:
    mid = (low+high)//2
    if l[mid] == key:
        print("element is found")
        c=1
        break
    elif l[mid] > key:
        high = mid-1
    else:
        low = mid+1
if c==0:
    print("not found")
