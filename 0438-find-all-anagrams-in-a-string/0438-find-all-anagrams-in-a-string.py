class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            cp = Counter(p)
            dic=defaultdict(int)
            left = 0
            right = 0
            result=[]
            while right < len(s):
                if right >= len(p):
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        del dic[s[left]]
                    left += 1
                dic[s[right]] += 1
                right += 1
                if dic == cp:
                    result.append(left)
            return result
            

          
            
       
                
                
                
                
                 
                
                
                
             
        
        
            
   
        