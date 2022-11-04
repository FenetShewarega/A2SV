class Solution:
    def lengthOfLongestSubstring(self, s):
        mx=0
        left=0
        right =0
        dic=defaultdict(int)
        for right in range(len(s)):
            while s[right] in dic:
                del dic[s[left]]
                left+=1
            dic[s[right]]+=1
            mx=max(mx,right-left+1)
        return mx    