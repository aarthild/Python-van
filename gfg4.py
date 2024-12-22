class Solution:   
    def peakElement(self,arr):
        # Code here
        for i in range(0, len(arr)):
            if i==0 and len(arr)>i+1:
                if arr[i]>=arr[i+1]:
                    return i
            elif i==len(arr)-1:
                if arr[i]>=arr[i-1]:
                    return i
            else:
                if arr[i] >= arr[i-1] and arr[i]>=arr[i+1]:
                    return i
        
        return False
