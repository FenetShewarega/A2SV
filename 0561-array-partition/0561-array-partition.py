class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        mx=0
        for i in range(len(nums)):
            if i%2==0:
                mx+=nums[i]
        return mx        
            
       