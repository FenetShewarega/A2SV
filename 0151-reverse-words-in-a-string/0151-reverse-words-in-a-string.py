class Solution:
    def reverseWords(self, s: str) -> str:
            s=s.split() 
            r=0
            l=len(s)-1
            for r in range(len(s)//2):
                s[l],s[r ] = s[r],s[l]
                l-=1
            return " ".join(s)   
            

                
        