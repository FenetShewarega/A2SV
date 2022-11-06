class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total=0
        lis=[]
        for i in range(len(gain)):
            total+=gain[i]
            lis.append(total)
        if max(lis) > 0:
            return max(lis)
        else:
            return 0
            
            
             