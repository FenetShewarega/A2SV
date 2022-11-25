class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0
        right = 0
        while right < len(s) and left < len(t):
            if s[right] == t[left]:
                right+=1
                left+=1
                
            else:
                left+=1
        return right == len(s)       
            
                
        