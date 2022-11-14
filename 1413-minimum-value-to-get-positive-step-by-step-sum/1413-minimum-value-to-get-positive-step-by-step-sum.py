class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total=0
        prefix=[]
        for i in nums:
            total+=i
            prefix.append(total)
           
        x= min(prefix)
        if x < 0:
            return (-x + 1)
        else:
            return 1
            
    
    