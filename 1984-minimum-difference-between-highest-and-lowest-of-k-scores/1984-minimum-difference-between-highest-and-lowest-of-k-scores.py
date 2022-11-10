class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l=0
        nums.sort()
        lis=[]
        for r in range((k-1),len(nums)):
            # print(nums)
            x = nums[r] - nums[l] 
            lis.append(x)
            l+=1
        return (min(lis))    
            
