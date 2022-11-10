class Solution:
    def findLongestWord(self, s: str, dic: List[str]) -> str:
#         "abpcplea"
#                l
#         ["ale","apple","monkey","plea"] 3            r
     
        # mx=0
        ans=""
        # (m + k)* n 
        for i in dic : 
            count=0
            l = 0 
            for r in range(len(i)):
                while l<len(s) and i[r] != s[l] : 
                    l+=1
                if l < len(s)  :
                    count+=1
                l+=1
            if len(i) == count and count >= len(ans) :    
                if len(ans) == count :
                    if ans > i:
                        ans =i
                    continue
                ans=i
        return ans               
                
       
            
                
                
                
            
          
                
                
                
                
                
                
                
    
        
        