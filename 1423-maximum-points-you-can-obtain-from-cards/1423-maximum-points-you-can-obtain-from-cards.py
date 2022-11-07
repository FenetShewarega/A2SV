class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        total =sum(cp)
        _sum = sum(cp[:len(cp) - k])
        mn = _sum
        l = 0
        r = len(cp) - k
        while r < len(cp):
            _sum-=cp[l]
            _sum+=cp[r]
            mn = min(_sum,mn)
            r+=1
            l+=1
        return total - mn
            
        
        
     
        
        