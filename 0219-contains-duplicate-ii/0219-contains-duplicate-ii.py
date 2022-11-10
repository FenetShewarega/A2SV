class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
          
            j=0
            if k >= len(nums):
                k = len(nums) -1
            duplicate = defaultdict(int)
            for i in range(k+1):
                duplicate[nums[i]] += 1
                if duplicate[nums[i]] > 1 :
                    return True
           
           
            for i in range(k+1,len(nums)):
               
                duplicate[nums[i]]+=1
                duplicate[nums[j]]-=1
                j+=1
                if duplicate[nums[i]] > 1 :
                    return True
                
            return False     
                
                    
                
                    
                