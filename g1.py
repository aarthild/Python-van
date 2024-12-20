class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        #code here
        a=arr1.sort()
        b=arr2.sort()
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
        return True  
