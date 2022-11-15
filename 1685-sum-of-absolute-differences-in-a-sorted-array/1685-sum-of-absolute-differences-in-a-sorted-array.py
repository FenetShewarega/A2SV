class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
      
        prefix=[0]
        suffix=[0]
        c=0
        for i in range(1,len(nums)):
            c+=nums[i-1]
            prefix.append(c)
        c=0
        for i in range(len(nums)-2,-1,-1):
            c+=nums[i+1]
            suffix.append(c)    
        suffix.reverse()    
        ans=[]
        for i in range(len(nums)):
            c1=(nums[i]*i)-(prefix[i])
            c2=(suffix[i])-(nums[i]*(len(nums)-i-1))
            ans.append(c1+c2)
        return ans    
        