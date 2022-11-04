class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left= 0
        right =0
        count=0
        mul=1
        while right < len(nums) and left <len(nums):
            if mul*nums[right] < k:
                mul*=nums[right] 
                count+=(right-left)+1
                right+=1
            else:
                mul/=nums[left]
                left+=1
        return count
#     [10,5,2,6]
#      l
#           r
#      mul=5       
#      count = 3       
#     0-0 +1           
#     1-0+1 =2            
                 
                
             