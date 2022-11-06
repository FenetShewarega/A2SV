class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # [5,6,2,7,4]
         
        nums.sort()
        i=0
        j=len(nums)-1
        mx=(nums[j]*nums[j-1])-(nums[i]*nums[i+1])
        return mx
            
            
            
            
        
        