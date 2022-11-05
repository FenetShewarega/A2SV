class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right =0
        mx=0
        ans=0
        for right in range(len(nums)):
            if nums[right]==1:
                mx+=1
                ans = max(ans,mx)
            else:
                mx = 0
        return ans
            
                
        0,0,0
        