class Solution:
    def removeStars(self, s: str) -> str:
        # s="leet**cod*e"
        # stack=[l e e t ]
        stack=[]
        for i in s:
            if stack and ( i == "*" ):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)       
                
            