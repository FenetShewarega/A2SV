class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort ()
       
        j=len(nums)-1
        mx=(nums[j]-1)*(nums[j-1]-1)
        return mx
        
        