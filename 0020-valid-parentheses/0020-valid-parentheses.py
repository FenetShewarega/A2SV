class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
       
        stack = []
        Map = { ")": "(", "}" : "{", "]" : "[" }
        for c in s :
            if c in Map :
                if stack and stack[-1] == Map[c] :
                    stack.pop()
                else :
                    return False
            else:
                stack.append(c)
        if not stack: 
            return True
        else:
            return False
               