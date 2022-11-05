class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right =0
        mx=0
        for right in range(len(nums)):
            if nums[right] != 1 :
                left= right + 1
            mx=max(mx,right - left + 1)
        return mx
            
                
        0,0,0
        