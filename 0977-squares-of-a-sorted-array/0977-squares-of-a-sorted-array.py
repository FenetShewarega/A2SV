class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
   
        left=0
        for right in range(len(nums)):
            nums[right] = nums[right]*nums[right]
        print(nums)    
        nums.sort() 
        
        return(nums)
            
            
            
        
        