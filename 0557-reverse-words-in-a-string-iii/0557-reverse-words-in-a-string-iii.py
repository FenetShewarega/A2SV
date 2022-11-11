class Solution:
    def reverseWords(self, s: str) -> str:
        list_reversed=[]
        
        s= s.split()
        print(s)
        for word in s:
            left=0
            right = len(word)-1
            word=list(word)
            while left < right:
                temp=word[left]
                word[left]=word[right]
                word[right]=temp
                left+=1
                right-=1
            word = (''.join(word))
            list_reversed.append(word)
        return(' '.join(list_reversed)) 
        #     list_reversed.append(word)
        # return " ".join(list_reversed)    

        