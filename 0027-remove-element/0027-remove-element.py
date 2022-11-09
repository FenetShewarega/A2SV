class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         [3,2,2,3]
#          l
#            r
         
# #         val = 3
        l=0
        r=0
        count = 0
        while r <len(nums):
            if nums[r] != val :
                nums[l]=nums[r] 
                l+=1
            
            r+=1
        return l
                
           
                

        
        