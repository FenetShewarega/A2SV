class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        len_prefix=0
        for i , j in intervals:
            len_prefix=max(len_prefix,j)
        prefix= [0] * (len_prefix + 2)   
        for i,j in intervals:
            prefix[i]+=1
            prefix[j + 1]-=1
        for x in range(1,len(prefix)):
            prefix[x]+=prefix[x-1]
        return max(prefix)    
        
          
                
          
           