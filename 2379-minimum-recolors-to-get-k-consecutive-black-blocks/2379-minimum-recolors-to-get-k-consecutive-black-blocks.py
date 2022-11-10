class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        l=0
        count=0
        ans=len(b)+1
        for r in range(len(b)): 
            if b[r]=="W":
                count+=1
            if r - l + 1 == k :
                ans=min(ans,count)
                if b[l] == "W":
                    count-=1
                l+=1    
        return ans          
