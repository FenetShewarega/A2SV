class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         # nums = [1,1,2]
         #           l
         #             r
        
        right=0
        left=0
        while right < len(nums):
            if nums[left]!= nums[right]:
                left+=1
                
                nums[left]=nums[right]
            right+=1   
        return left+1        
                
                
                
              
 
                
            
        
        
        
        
        
        