class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], X: int) -> int:
     
      
   
        total=0
        for right in range(len(g)):
            if g[right] == 0:
                total += c[right]
        for R in range(X):
            if g[R] == 1:
                total+= c[R]
        max_total = total    
        i=0
        j=X
        while j <  len(c):
            if g[j] == 1 :
                total += c[j]
            if g[i] == 1:
                total -= c[i]
            if total > max_total :
                max_total = total
            i+=1
            j+=1
        return max_total   
    
