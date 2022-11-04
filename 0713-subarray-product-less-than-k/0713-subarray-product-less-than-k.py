class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left= 0
        right =0
        count=0
        mul=1
        for right in range(len(nums)):
            mul *= nums[right]
            while mul >= k and left <= right:
                mul/=nums[left]
                left+=1
            count += (right- left) + 1    
        return count   
                
                
#     [10,5,2,6]
#      l
#           r
#      mul=5       
#      count = 3       
#     0-0 +1           
#     1-0+1 =2            
                 
                
             