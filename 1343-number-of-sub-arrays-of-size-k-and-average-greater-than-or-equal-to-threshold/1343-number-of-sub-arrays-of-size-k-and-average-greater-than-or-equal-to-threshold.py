class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
         # [2,2,2,2,5,5,5,8]
        total=0
        count=0
        left =0
        right=0
        for right in  range(k):
            total+=arr[right]
        if total / k >= threshold:
            count+=1
        right = k
        while right < len(arr):
            total+=arr[right]
            total-=arr[left]
            if total / k >= threshold:
                count+=1
            right+=1
            left+=1
        return count   
            
            
            
            
          
               
        