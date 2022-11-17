class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
       
        dic = defaultdict(int)
        ans = defaultdict(int)
        mx=0
        right = 0
        left = 0
        while right < len(s):
            dic[s[right]]+=1
            right+=1
            while right - left  >= minSize and right -left  <= maxSize:
                if len(dic) <= maxLetters:
                    ans[s[left:right]] += 1
                    
                dic[s[left]]-=1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left+=1
                
       
        for values in ans.values():
            mx=max(mx,values)
        return mx 
    
