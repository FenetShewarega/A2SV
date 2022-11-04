class Solution:
    def lengthOfLongestSubstring(self, s):
       
        # abcabcbb
        #      l
        #        r   
        # dic  { a:1
        #       b:1
        #       c:1
        #      }
        mx=0
        left=0
        right =0
        dic=defaultdict(int)
        while  right < len(s):
            
            if s[right] not in dic:
                dic[s[right]] +=1
                right+=1
                mx=max(mx,right - left)
            else :
                del dic[s[left]]
                left+=1
        return mx        
            