class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        ws=0
        mx=0
        for right in range(len(nums)):
            ws += nums[right]
            while nums[right] * (right-left+1) > k + ws:
                ws -= nums[left]
                left+=1
            mx =max(mx,right-left+1)
        return mx   
            
                
       

          
            