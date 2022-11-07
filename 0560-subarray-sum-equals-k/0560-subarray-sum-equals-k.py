class Solution(object):
    def subarraySum(self, nums, k):
      
        prefixsum = {0:1}
        sumM = 0
        ans = 0
        
        for num in nums:
            sumM += num
            
            diff = sumM - k 
            ans += prefixsum.get(diff,0)
            if sumM in prefixsum:
                prefixsum[sumM] += 1
                
            else:
                prefixsum[sumM] = 1
                        
        return ans