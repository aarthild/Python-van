#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        arr.sort()
        c=0
        for i in range(len(arr)):
            if arr[i]==k:
                c+=1
        if c>=1:
            return True
        return False
