class Solution(object):
    def pivotIndex(self, nums):
        total=0
        for i in nums:
            total+=i
        
        cum = 0
        
        for i in range(len(nums)):
            
            if cum == (total - cum - nums[i]):
                return i
            else:
                cum += nums[i]
        
        return -1
