class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             if nums[i] % 2 != 0:
#                 x = nums[i] 
#                 nums.append(x)
#                 nums.remove(x)
                
#         return nums        
        o=[]
        e=[]
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                o.append(nums[i])
            else:
                e.append(nums[i])
        return (e+o)        