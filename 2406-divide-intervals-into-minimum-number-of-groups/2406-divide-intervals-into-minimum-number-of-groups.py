class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        prefix= [0] * (1000002)   
        for i,j in intervals:
            prefix[i]+=1
            prefix[j + 1]-=1
            
        for x in range(1,len(prefix)):
            prefix[x]+=prefix[x-1]
        return max(prefix)    
        
          
                
          
           