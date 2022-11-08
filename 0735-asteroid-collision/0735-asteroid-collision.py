class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack=[]
        i=0
        while  i < len(ast):
            if stack and (stack[-1] >0 and ast[i] < 0):
                if (abs(ast[i]) > stack[-1]):
                    stack.pop()
                elif (abs(ast[i]) < stack[-1]):
                    i+=1
                else:
                    stack.pop()
                    i+=1
            else:
                      stack.append(ast[i])
                      i+=1
        return stack           
                    
              
                    
       