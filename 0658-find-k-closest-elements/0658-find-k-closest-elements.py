class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
         
        
          
                
        startPointer = 0
        endPointer = len(arr) - 1
        
        while endPointer - startPointer >= k:
            if abs(arr[startPointer] - x) <= abs(arr[endPointer] - x):
                endPointer -= 1
            else:
                startPointer += 1
		
        return arr[startPointer: endPointer + 1]
                
                
            
            
        