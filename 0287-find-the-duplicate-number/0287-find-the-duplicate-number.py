class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         r=0
#         l=len(nums)
#         [0,1,4,2,2]
        
            nums.sort()
            j=1    
            for i in range(len(nums)):
                if  nums[i] == nums[j]:
                    return (nums[i])
                j+=1