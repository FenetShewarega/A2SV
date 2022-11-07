class Solution(object):
    def minPairSum(self, nums):
        
        nums.sort()
        maxpair=0
        i = 0
        j = len(nums)-1
        while i < j:
            maxpair = max(maxpair, nums[i]+nums[j]) 
            i+=1
            j-=1
        return maxpair    
        """
        
        :type nums: List[int]
        :rtype: int
        """
        