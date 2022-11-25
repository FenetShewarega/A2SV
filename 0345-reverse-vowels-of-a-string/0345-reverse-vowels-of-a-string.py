class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left = len(s) - 1
        right=0
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        while right < len(s) and left > right:
            if s[right] in vowels :
                if s[left] in vowels:
                    s[right],s[left] = s[left],s[right]
                    left-=1
                    right+=1
                else:
                    left-=1
                    
            elif s[left] in vowels:
                if s[right] in vowels:
                    s[right],s[left] = s[left],s[right]
                    left-=1
                    right+=1
                else:
                    right+=1
            else:
                right+=1
                left-=1
        return ''.join(s)        
        