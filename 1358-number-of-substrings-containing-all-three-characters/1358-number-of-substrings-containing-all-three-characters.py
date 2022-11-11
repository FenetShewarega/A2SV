class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        right=0
        count=0
        counter=defaultdict(int)
        for right in range(len(s)):
            counter[s[right]]+=1
            while len(counter) == 3:
                count += len(s) - right
                counter[s[left]]-= 1
                if counter[s[left]]==0:
                    del  counter[s[left]]
                left+=1
        return count        
                                 
                                       